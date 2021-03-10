from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, Group, BaseUserManager, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.exceptions import ValidationError
from django.db import models


# Create Manager

class UserManager(BaseUserManager):

    def create_user(self, username, password, email):
        if not username:
            raise TypeError('Username must not be empty')
        if not password:
            raise TypeError('Password must not be empty')
        if not email:
            raise TypeError('Email must not be empty')
        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, email):
        user = self.create_user(username, password, email)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        max_length=150,
        unique=True,
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        validators=[username_validator],
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )
    first_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='avatar/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['password', 'email']
    objects = UserManager()

    def __str__(self):
        return self.username
