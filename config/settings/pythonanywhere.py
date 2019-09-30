import logging.config

from config.settings.common import *  # noqa

SECRET_KEY = env.str('DJANGO_SECRET_KEY')

DEBUG = False

# security
CSRF_COOKIE_SECURE = env.bool('CSRF_COOKIE_SECURE', True)
SECURE_BROWSER_XSS_FILTER = env.bool('SECURE_BROWSER_XSS_FILTER', True)
SECURE_HSTS_SECONDS = env.int('SECURE_HSTS_SECONDS', 60 * 60 * 24 * 3)  # 3 day
SESSION_COOKIE_SECURE = env.bool('SESSION_COOKIE_SECURE', True)
SESSION_COOKIE_HTTPONLY = env.bool('SESSION_COOKIE_HTTPONLY', True)

LOGGING_CONFIG = None
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '[%(levelname)s] [%(asctime)s] [%(name)s] '
                      '[%(process)d] [%(thread)d] %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG'
        },
        # don't simplify with only 'django' logger name
        # so we can keep track of logger names
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False
        },
        'django.middleware': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}

# http.client.HTTPConnection.debuglevel = 1
logging.config.dictConfig(LOGGING)
