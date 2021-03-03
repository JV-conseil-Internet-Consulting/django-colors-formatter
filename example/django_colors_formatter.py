from django_colors_formatter import DjangoColorsFormatter


class CustomDjangoColorsFormatter(DjangoColorsFormatter):
    """ Subclassing the formatter.

    In `settings.py`:
    ```py
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'console': {
                '()': 'django_colors_formatter.CustomDjangoColorsFormatter',
                'format': '{asctime} {levelname} {name} {message}',
                'style': '{',
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'console'
            },
            'mail_admins': {
                'level': 'ERROR',
                'class': 'django.utils.log.AdminEmailHandler',
                'include_html': True,
            }
        },
        'root': {
            'handlers': ['console', 'mail_admins'],
            'level': 'INFO',
        },
    }
    ```
    """

    def configure_style(self, style):
        style.DEBUG = style.HTTP_NOT_MODIFIED
        style.INFO = style.HTTP_INFO
        style.WARNING = style.HTTP_NOT_FOUND
        style.ERROR = {
            'fg': 'yellow',
            'bg': 'blue',
            'opts': ('blink',),
        }
        style.CRITICAL = style.HTTP_SERVER_ERROR
        return style
