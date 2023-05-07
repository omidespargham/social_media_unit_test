
class BaseLoggingMixin:
    def initial(self, request, *args, **kwargs):
        print("/"*100)
        super().initial(request, *args, **kwargs)

    def finalize_response(self, request, response, *args, **kwargs):
        return super().finalize_response(request, response, *args, **kwargs)

