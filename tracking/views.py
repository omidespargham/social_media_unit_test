from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .mixins import LoggingMixin

class TrackingHomeView(LoggingMixin,APIView):
    logging_methods = ["GET","POST"]
    sensitive_fields = {"pass"}
    # sensetive_fields = {"something"} ===> in chizi ast ke ba estefade az oon mitoonim
    # biayam va yeseri data haro daroone log moon zakhire nakonim mesle pass va ..
    # va in bayad piade sazi beshe (unittest.sensetivefileds) 
    def get(self,request):
        return Response(data={"this is the response !"})

