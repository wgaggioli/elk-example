import logging.config
import random
import time

import structlog
from flask import (
    Flask,
    request,
    g,
    got_request_exception,
)

from settings import LOGGING_CONFIG, STRUCTLOG_PROCESSORS

app = Flask('elk_example')
logger = structlog.get_logger('elk_example_json')


@app.route('/')
def index():
    app.struct_log.info('hello world')
    return 'boogars'


@app.route('/another')
def another():
    sleepy_time = random.gauss(1., 0.3)
    time.sleep(max([0., sleepy_time]))
    return 'candy canes'


@app.route('/error')
def error():
    1/0

@app.before_request
def _on_request_start():
    app.struct_log.bind(
        verb=request.method,
        path=request.path,
        headers=dict(request.headers),
        environ=request.environ,
        form=request.form,
        query_args=request.args,
    )
    g.time_started = time.time()


@app.teardown_request
def _on_request_finished(exception=None):
    app.struct_log.info(
        'request-complete',
        duration=time.time() - g.time_started,
    )

#
# def _log_exception(sender, exception, exc_info=None, **extra):
#     app.struct_log.error(exc_info=exception)
#
#
# got_request_exception.connect(_log_exception, app)


if __name__ == "__main__":
    app.logger.info(app.logger_name)  # DO NOT REMOVE -- needed to init logger
    logging.config.dictConfig(LOGGING_CONFIG)
    structlog.configure(
        processors=STRUCTLOG_PROCESSORS,
        context_class=structlog.threadlocal.wrap_dict(dict),
        logger_factory=structlog.stdlib.LoggerFactory(),
    )
    app.struct_log = logger.new()
    app.run(host="0.0.0.0", use_reloader=True)
