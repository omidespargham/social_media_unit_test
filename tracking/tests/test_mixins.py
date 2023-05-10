from django.test import override_settings
from rest_framework.test import APIRequestFactory,APITestCase
from .views import MockLoggingView,MockNoLoggingView
from tracking.models import APIRequestlog
# from tracking.models import 

@override_settings(ROOT_URLCONF= "tracking.tests.urls")
class TestLoggingMixin(APITestCase):
    def test_nologging_no_log_created(self):
        response = self.client.get("/nologging/")
        self.assertEqual(APIRequestlog.objects.all().count(),0)

    def test_logging_log_created(self):
        self.client.get("/logging/")
        self.assertEqual(APIRequestlog.objects.all().count(),1)

    def test_log_path(self):
        self.client.get("/logging/")
        self.assertEqual(APIRequestlog.objects.first().path,"/logging/")

    def test_log_ip_remote(self):
        request = APIRequestFactory().get("/logging/")
        request.META['REMOTE_ADDR'] = '127.0.0.9'
        MockLoggingView.as_view()(request).render()
        log = APIRequestlog.objects.first()
        self.assertEqual(log.remote_addr,"127.0.0.9")

    def test_log_ip_remote_list(self):
        request = APIRequestFactory().get("/logging/")
        request.META['REMOTE_ADDR'] = '127.0.0.9,127.0.0.8'
        MockLoggingView.as_view()(request).render()
        log = APIRequestlog.objects.first()
        self.assertEqual(log.remote_addr,"127.0.0.9")

    def test_log_ip_remote_v4_with_port(self):
        request = APIRequestFactory().get("/logging/")
        request.META['REMOTE_ADDR'] = '127.0.0.9:8000'
        MockLoggingView.as_view()(request).render()
        log = APIRequestlog.objects.first()
        self.assertEqual(log.remote_addr,"127.0.0.9")
        '2001:0db8:85a3:0000:0000:8a2e:0370:7334'

    def test_log_ip_remote_v6(self):
        request = APIRequestFactory().get("/logging/")
        request.META['REMOTE_ADDR'] = '2001:0db8:85a3:0000:0000:8a2e:0370:7334'
        MockLoggingView.as_view()(request).render()
        log = APIRequestlog.objects.first()
        self.assertEqual(log.remote_addr,'2001:db8:85a3::8a2e:370:7334')

    def test_log_ip_remote_v6_loopback(self):
        request = APIRequestFactory().get("/logging/")
        request.META["REMOTE_ADDR"] = "::1"
        MockLoggingView.as_view()(request).render()
        log = APIRequestlog.objects.first()
        self.assertEqual(log.remote_addr,"::1")

    def test_log_ip_remote_v6_with_port(self):
        request = APIRequestFactory().get("/logging/")
    
