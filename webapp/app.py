import logging.config

from flask import Flask

from settings import LOGGING_CONFIG

app = Flask('elk_example')

@app.route('/')
def index():
    app.logger.info('hi mom')
    return 'boogars'

if __name__ == "__main__":
    app.logger.info(app.logger_name)
    logging.config.dictConfig(LOGGING_CONFIG)
    app.run(host="0.0.0.0", debug=True)
