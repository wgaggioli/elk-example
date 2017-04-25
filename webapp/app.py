import logging.config

import structlog
from flask import (
    Flask,
    request,
    request_started,
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
    app.struct_log.info('another')
    return 'candy canes'


@app.route('/error')
def error():
    1/0


def _init_logger(sender, **extra):
    app.struct_log.bind(
        verb=request.method,
        path=request.path,
        headers=dict(request.headers),
        environ=request.environ,
        form=request.form,
        query_args=request.args,
    )

request_started.connect(_init_logger, app)


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
