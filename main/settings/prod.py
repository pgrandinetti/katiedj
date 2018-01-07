from .common import *

DEBUG = False
ALLOWED_HOSTS = ['*']

CONN_MAX_AGE = None

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

#ADMINS = [('', '')]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticRoot')

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'

# Here one should
# - set robust remote Database Layer
# - set the EMAIL_BACKEND
# - set logging system for production
# Examples taken from ./dev.py, not-production-ready!
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'traffic_server_db.sqlite3'),
    }
}
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}
