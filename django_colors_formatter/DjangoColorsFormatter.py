import logging
import sys

from django.core.management.color import color_style


class DjangoColorsFormatter(logging.Formatter):
    """ See Syntax coloring and DJANGO_COLORS
    https://docs.djangoproject.com/en/3.1/ref/django-admin/#syntax-coloring
    """

    def __init__(self, *args, **kwargs):
        super(DjangoColorsFormatter, self).__init__(*args, **kwargs)
        self.style = self.configure_style(color_style())

    def configure_style(self, style):
        """ Available style choices are:
        `['ERROR', 'SUCCESS', 'WARNING', 'NOTICE', 'SQL_FIELD', 'SQL_COLTYPE', 'SQL_KEYWORD', 'SQL_TABLE', 'HTTP_INFO', 'HTTP_SUCCESS', 'HTTP_REDIRECT', 'HTTP_NOT_MODIFIED', 'HTTP_BAD_REQUEST', 'HTTP_NOT_FOUND', 'HTTP_SERVER_ERROR', 'MIGRATE_HEADING', 'MIGRATE_LABEL', 'ERROR_OUTPUT']`
        """
        # print(list(style.__dict__.keys()))

        style.DEBUG = style.HTTP_NOT_MODIFIED
        style.INFO = style.HTTP_INFO
        style.WARNING = style.HTTP_NOT_FOUND
        style.ERROR = style.ERROR
        style.CRITICAL = style.HTTP_SERVER_ERROR
        return style

    def format(self, record):
        message = logging.Formatter.format(self, record)
        if sys.version_info[0] < 3:
            if isinstance(message, str):  # Python 3 renamed the unicode type to str: https://stackoverflow.com/a/19877309/2477854
                message = message.encode('utf-8')
        colorizer = getattr(self.style, record.levelname, self.style.HTTP_SUCCESS)
        return colorizer(message)


class CustomDjangoColorsFormatter(DjangoColorsFormatter):
    """
    Subclassing the formatter: free-form configuration
    https://github.com/sdurioanalytics/django-colors-formatter#subclassing-the-formatter-free-form-configuration
    """

    def configure_style(self, style):
        style.DEBUG = style.HTTP_INFO
        style.INFO = style.HTTP_NOT_MODIFIED
        style.WARNING = style.WARNING
        style.ERROR = style.ERROR
        style.CRITICAL = style.HTTP_SERVER_ERROR
        return style
