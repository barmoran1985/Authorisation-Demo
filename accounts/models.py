from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, UserManager


# Create your models here.

class AccountUserManager(UserManager):
    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        """

        :param username:
        :param email:
        :param password:
        :param is_staff:
        :param is_superuser:
        :param extra_fields:
        :return:
        """

        now = timezone.now()
        if not email:
            raise ValueError('the given username must be set')

        email = self.normalize_email(email)
        user = self.model(username=email, email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


class User(AbstractUser):
    objects = AccountUserManager()

