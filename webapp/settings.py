import structlog

LOGGING_FILE = '/var/log/app.log'
STRUCTURED_LOGGING_FILE = '/var/log/app_structured.log'
LOGGING_CONFIG = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '%(asctime)s %(levelname)s %(name)s %(message)s'
        }
    },
    'handlers': {
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOGGING_FILE,
            'formatter': 'default'
        },
        'structured_file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': STRUCTURED_LOGGING_FILE,
        }
    },
    'loggers': {
        'root': {
            'level': 'WARN',
            'handlers': ['file']
        },
        'elk_example': {
            'level': 'INFO'
        },
        'elk_example_json': {
            'level': 'INFO',
            'handlers': ['structured_file']
        }
    }
}

_METHOD_TO_NAME = {
    'critical': 'CRITICAL',
    'exception': 'ERROR',
    'error': 'ERROR',
    'warn': 'WARNING',
    'warning': 'WARNING',
    'info': 'INFO',
    'debug': 'DEBUG',
    'notset': 'NOTSET',
}


def add_log_level(logger, method_name, event_dict):
    event_dict['level'] = _METHOD_TO_NAME[method_name]
    return event_dict


STRUCTLOG_PROCESSORS = [
    structlog.stdlib.filter_by_level,
    structlog.stdlib.add_logger_name,
    add_log_level,
    structlog.stdlib.PositionalArgumentsFormatter(),
    structlog.processors.TimeStamper(fmt='iso', key='@timestamp'),
    structlog.processors.StackInfoRenderer(),
    structlog.processors.format_exc_info,
    structlog.processors.JSONRenderer(),
]
