import logging.config

from flask import Flask

from settings import LOGGING_CONFIG

app = Flask('elk_example')


@app.route('/')
def index():
    app.logger.info('hello world')
    return 'boogars'


@app.route('/error')
def error():
    1/0


if __name__ == "__main__":
    app.logger.info(app.logger_name)  # DO NOT REMOVE -- needed to init logger
    logging.config.dictConfig(LOGGING_CONFIG)
    app.run(host="0.0.0.0", use_reloader=True)
