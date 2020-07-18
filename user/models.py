from django.contrib.auth.models import User as DjangoUser
from django.utils.translation import gettext_lazy as _
from django.db import models


class User(models.Model):
    user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='profiles')

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.username
