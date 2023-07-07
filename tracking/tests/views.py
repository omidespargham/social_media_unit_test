from rest_framework.views import APIView
from rest_framework.response import Response
from tracking.mixins import LoggingMixin
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class MockNoLoggingView(APIView):
    def get(self,request):
        return Response("no logging")
    
class MockLoggingView(LoggingMixin,APIView):
    def get(self,request):
        return Response("logging the view")


class MockExplicitLoggingView(LoggingMixin, APIView):
    logging_methods = ['POST']

    def get(self, request):
        return Response('no logging')
    def post (self, request):
        return Response('with logging')

class MockCustomCheckLoggingView(LoggingMixin, APIView):
    def should_log(self, request, response):
        return 'log' in response.data

    def get(self, request):
        return Response('with logging')
    def post(self, request):
        return Response('no recording')
    

class MockSessionAuthLoggingView(LoggingMixin,APIView):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response('with session auth logging')

class MockTokenAuthLoggingView(LoggingMixin, APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated)

    def get(self, request):
        return Response('with token auth logging')
    

class MockSensitiveFieldsLoggingView(LoggingMixin ,APIView):
    sensitive_fields = {"mY_fiEld"}

    def get(self,request):
        return Response("with logging")
    

class MockInvalidCleanedSubstituteLoggingView(LoggingMixin ,APIView):
    CLEANED_SUBSTITUTE = 1
