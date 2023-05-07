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