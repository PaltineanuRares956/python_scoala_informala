from django.contrib.auth.backends import BaseBackend
from users.models import User


class Backend(BaseBackend):
    pass
    # def authenticate(self, request, **kwargs):
#
    #     if 'username' not in kwargs:
    #         raise ValueError('Invalid username')
    #     if 'password' not in kwargs:
    #         raise ValueError('Invalid password')
#
    #     username = kwargs.get('username')
    #     password = kwargs.get('password')
    #     try:
    #         user = User.objects.get(username=username, password=password)
    #     except User.DoesNotExist:
    #         return None
    #     return user
