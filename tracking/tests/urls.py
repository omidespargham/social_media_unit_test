from django.urls import path
from . import views


urlpatterns = [
    path("nologging/",views.MockNoLoggingView.as_view(),name="no_logging"),
    path("logging/",views.MockLoggingView.as_view(),name="logging"),
]
