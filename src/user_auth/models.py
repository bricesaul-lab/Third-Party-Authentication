from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser
from .manager import CustomUserManager



# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    fname           = models.TextField(max_length=20)
    lname           = models.TextField(max_length=20)
    email           = models.EmailField(_('email address'), unique=True, max_length= 60)
    username        = models.CharField(max_length=30, unique=True)
    verified        = models.BooleanField(default=False)
    display         = models.ImageField(upload_to='images/')
    accounts        = models.JSONField(default = dict,null=True, blank=True)


    is_superuser    = models.BooleanField(default = False)
    is_staff        = models.BooleanField(default = False)
    is_active       = models.BooleanField(default = True)
    last_login      = models.DateTimeField(_('last login'),default = timezone.now)
    date_joined     = models.DateTimeField(_('date joined'),  default = timezone.now)
    

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username','fname','lname']

    objects = CustomUserManager()

    def __str__(self):
        return "{}({})".format(self.username,self.email)