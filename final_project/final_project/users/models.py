from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self, email, username, password):
        if not username:
            raise ValueError('Username not defined')
        if not password:
            raise ValueError('Password not defined')
        if not email:
            raise ValueError('Email not defined')

        user = self.model(
            username=username,
            email=email
        )

        user.set_password(password)
        # user.password = password
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, email):
        if not username:
            raise ValueError('Username not defined')
        if not password:
            raise ValueError('Password not defined')
        if not email:
            raise ValueError('Email not defined')
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255,
                                verbose_name='Username:',
                                blank=False,
                                unique=True,
                                default='username')
    email = models.EmailField(max_length=255,
                              verbose_name='Email:',
                              unique=True,
                              default='email@email.com')
    password = models.CharField(max_length=255,
                                blank=False,
                                null=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']
    objects = UserManager()

    class Meta:
        db_table = 'users'

    # @property
    # def is_staff(self):
    #     return self.is_staff
#
    # @property
    # def is_admin(self):
    #     return self.is_admin
#
    # @property
    # def is_active(self):
    #     return self.is_active
#
    def get_username(self):
        return self.username

    def __str__(self):
        return self.username
