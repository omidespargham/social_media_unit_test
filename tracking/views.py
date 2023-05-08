from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .mixins import LoggingMixin

class TrackingHomeView(LoggingMixin,APIView):
    logging_methods = ["GET","POST"]

    def get(self,request):
        return Response(data={"this is the response !"})

