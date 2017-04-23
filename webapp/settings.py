LOGGING_FILE = '/var/log/app.log'
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
            'level': 'INFO',
            'filename': LOGGING_FILE,
            'formatter': 'default'
        }
    },
    'loggers': {
        'root': {
            'level': 'INFO',
            'handlers': ['file']
        },
        'elk_example': {
            'level': 'INFO',
            'handlers': ['file']
        }
    }
}
