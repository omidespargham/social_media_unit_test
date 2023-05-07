from django.utils.timezone import now


class BaseLoggingMixin:
    def initial(self, request, *args, **kwargs):
        self.log = {
            "requested_at":now(),
        }
        super().initial(request, *args, **kwargs)

    def finalize_response(self, request, response, *args, **kwargs):
        response = super().finalize_response(request, response, *args, **kwargs)
        self.log.update({
            "remote_addr": self._get_ip_address(request),
            "view": self._get_view_name(request),
            "view_method":self._get_view_method(request),
            "path":self._get_path(request),

            }
        )
        print(self.log)
        self.handle_log()
        return response

    def handle_log(self):
        raise NotImplementedError
    
    def _get_ip_address(self,request):
        ipaddr = request.META.get("HTTP_X_FORWARDED_FOR",None)
        if ipaddr:
            ipaddr = ipaddr.split(",")[0]
        else:
            ipaddr = request.META.get("REMOTE_ADDR",'').split(",")[0]
        return ipaddr
    
    def _get_view_name(self,request):
        # self is <tracking.views.TrackingHomeView object at 0x10e26c9d0> object
        # you can get view name from it.
        method = request.method.lower()
        try:
            attribute = getattr(self,method)
            return (type(attribute.__self__).__method__ + '.' + type(attribute.__self__).__name__)
        except AttributeError:
            return None
    
    def _get_view_method(self,request):
        if hasattr(self,"action"):
            return self.action or None
        return request.method.lower()

    def _get_path(self,request):
        return request.path[:200]