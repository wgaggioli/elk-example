LOGGING_FILE = '/var/log/app.log'
LOGGING_CONFIG = {
    'version': 1,
    'handlers': {
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'INFO',
            'filename': LOGGING_FILE
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
