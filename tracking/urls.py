from tracking import views
from django.urls import path


app_name = 'tracking '
urlpatterns = [
	path('home/', views.TrackingHomeView.as_view(), name='tracking_home'),
]
