from django.urls import path
from . import views



# api/model.py 
from django.db import models
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)


# api/serializers.py 
from rest_framework import serializers
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["name", "roll", "city"]



# api/views.py 
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset= Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated] 

#urls.py 
from django.contrib import admin
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
from django.urls.conf import  path,include
# register viewset with router

router.register("studentapi2", StudentModelViewSet, basename="student")
# router.register("studentapi", , basename="student")


app_name = 'home'
urlpatterns = [
	path("about/<str:username>/",views.AboutView.as_view(),name="about"),
	path("writers/",views.WriterView.as_view(),name="writers"),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
	# path('post/<int:post_id>/<slug:post_slug>/', views.PostDetailView.as_view(), name='post_detail'),
	# path('post/delete/<int:post_id>/', views.PostDeleteView.as_view(), name='post_delete'),
	# path('post/update/<int:post_id>/', views.PostUpdateView.as_view(), name='post_update'),
	# path('post/create/', views.PostCreateView.as_view(), name='post_create'),
	# path('reply/<int:post_id>/<int:comment_id>/', views.PostAddReplyView.as_view(), name='add_reply'),
	# path('like/<int:post_id>/', views.PostLikeView.as_view(), name='post_like'),
]





