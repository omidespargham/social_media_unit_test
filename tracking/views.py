from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class TrackingHomeView(APIView):
    def get(self,request):
        return Response(data={"this is the response !"})

