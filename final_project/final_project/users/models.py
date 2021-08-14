from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self, username, password, email):
        if not username:
            raise ValueError('Username not defined')
        if not password:
            raise ValueError('Password not defined')
        if not email:
            raise ValueError('Email not defined')

        account = self.model(
            username=username,
            email=email
        )

        account.set_password(password)
        account.save(using=self._db)
        return account

    def create_superuser(self, username, password, email):
        if not username:
            raise ValueError('Username not defined')
        if not password:
            raise ValueError('Password not defined')
        if not email:
            raise ValueError('Email not defined')
        account = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password
        )
        account.is_staff = True
        account.is_admin = True
        account.is_superuser=True
        account.save(using=self._db)
        return account


class User(AbstractBaseUser, PermissionsMixin):
    is_admin = models.BooleanField(default=False)
    username = models.CharField(max_length=255,
                                verbose_name='Username:',
                                blank=False,
                                unique=True,
                                default='username')
    email = models.EmailField(max_length=255,
                              verbose_name='Email:',
                              unique=True,
                              default='email')
    password = models.CharField(max_length=255,
                                blank=False,
                                null=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'password']
    objects = UserManager()

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.username



