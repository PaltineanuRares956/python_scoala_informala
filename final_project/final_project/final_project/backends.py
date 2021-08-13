from django.contrib.auth.backends import BaseBackend


# TODO:
class Backend(BaseBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        pass
