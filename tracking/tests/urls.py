from django.urls import path
from . import views


urlpatterns = [
    path("nologging/",views.MockNoLoggingView.as_view(),name="no_logging"),
    path("logging/",views.MockLoggingView.as_view(),name="logging"),
    path("logging_explicit/",views.MockExplicitLoggingView.as_view()),
    path("logging_custom_check/",views.MockCustomCheckLoggingView.as_view()),
    path("session-auth-logging/",views.MockSessionAuthLoggingView.as_view()),
    path("token-auth-logging/",views.MockTokenAuthLoggingView.as_view()),
    path("sensitive-fields-logging/",views.MockSensitiveFieldsLoggingView.as_view()),
    path("invalid-cleaned-substitute-logging/",views.MockInvalidCleanedSubstituteLoggingView.as_view())
]
