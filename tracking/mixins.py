from .base_mixins import BaseLoggingMixin
from .base_models import BaseAPIRequestLog

class LoggingMixin(BaseLoggingMixin):
    def handle_log(self):
        BaseAPIRequestLog(**self.log).save()
        