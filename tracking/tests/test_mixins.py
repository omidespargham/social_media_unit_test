import ast
from django.test import override_settings
from rest_framework.test import APIRequestFactory,APITestCase
from .views import MockLoggingView,MockNoLoggingView
from tracking.models import APIRequestlog
from django.contrib.auth.models import User
from tracking.base_mixins import BaseLoggingMixin
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
        request.META["REMOTE_ADDR"] = "[::1]:1234"
        MockLoggingView.as_view()(request).render()
        log = APIRequestlog.objects.first()
        self.assertEqual(log.remote_addr,"::1")

    def test_log_ip_xforwarded(self):
        request = APIRequestFactory().get("/logging/")
        request.META['HTTP_X_FORWARDED_FOR'] = "127.0.0.8"
        MockLoggingView.as_view()(request).render()
        log = APIRequestlog.objects.first()
        self.assertEqual(log.remote_addr,"127.0.0.8")
        


    def test_log_ip_xforwarded_list(self):
        request = APIRequestFactory().get("/logging/")
        request.META['HTTP_X_FORWARDED_FOR'] = "127.0.0.8,127.0.0.9"
        MockLoggingView.as_view()(request).render()
        log = APIRequestlog.objects.first()
        self.assertEqual(log.remote_addr,"127.0.0.8")


    def test_log_host(self):
        self.client.get("/logging/")
        log = APIRequestlog.objects.first()
        self.assertEqual(log.host,'testserver')

    def test_log_method(self):
        self.client.get("/logging/")
        log = APIRequestlog.objects.first()
        self.assertEqual(log.method,"GET")
    

    def test_log_status_code(self):
        self.client.get("/logging/")
        log = APIRequestlog.objects.first()
        self.assertEqual(log.status_code,200)


    def test_logging_explicit_get_method(self):
        self.client.get("/logging_explicit/")
        self.assertEqual(APIRequestlog.objects.all().count(),0)

    def test_logging_explicit_post_method(self):
        self.client.post("/logging_explicit/")
        self.assertEqual(APIRequestlog.objects.all().count(),1)

    def test_logging_custom_check(self):
        self.client.post("/logging_custom_check/")
        self.client.get("/logging_custom_check/")
        self.assertEqual(APIRequestlog.objects.all().count(),1)

    def test_log_anon_user(self):
        self.client.get("/logging/")
        log = APIRequestlog.objects.first()
        self.assertEqual(log.user,None)

    def test_log_auth_user(self):
        User.objects.create_user(username="omid",email="omid@gmail.com",password="omid1234")
        user = User.objects.get(username="omid")
        self.client.login(username="omid",password="omid1234")
        self.client.get("/session-auth-logging/")
        
        log = APIRequestlog.objects.first()
        self.assertEqual(log.user,user)

    def test_log_params(self):
        self.client.get("/logging/",{"p1":"omid","p2":"omid2"})
        log = APIRequestlog.objects.first()
        self.assertEqual(ast.literal_eval(log.query_params),{"p1":"omid","p2":"omid2"})

    def test_Log_params_cleaned_from_personal_list(self):
        self.client.get('/sensitive-fields-logging/', {'api': '1234', 'capitalized': '12345', 'my_field': '1234564'})
        log = APIRequestlog.objects.first()
        self.assertEqual(ast.literal_eval(log.query_params), {
        'api': BaseLoggingMixin.CLEANED_SUBSTITUTE,
        'capitalized': '12345',
        'my_field': BaseLoggingMixin.CLEANED_SUBSTITUTE
        })


        