from django.db import models
from django.contrib.auth.models import Group, AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    fullname = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.username


class CustomGroup(Group):
    class Meta:
        proxy = True
        app_label = 'account'
        verbose_name = 'Group'
