from django.contrib import admin
from .models import APIRequestlog

class APIRequestlogAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "requested_at",
        "response_ms",
        "status_code",
        "user",
        "view_method",
        "path",
        "remote_addr",
        "host",
        "query_params",
        )


admin.site.register(APIRequestlog,APIRequestlogAdmin)

# Register your models here.
