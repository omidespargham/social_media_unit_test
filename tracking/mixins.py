from .base_mixins import BaseLoggingMixin
from .models import APIRequestlog 

class LoggingMixin(BaseLoggingMixin):
    def handle_log(self):
        APIRequestlog(**self.log).save()
        