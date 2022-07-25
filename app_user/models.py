from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('user'))
    city = models.CharField(max_length=40, default=None, null=True, verbose_name=_('city'))
    date_of_birth = models.DateField(default=None, null=True, verbose_name=_('date of birth'))
    hobby = models.TextField(default=None, null=True, verbose_name=_('hobby'))

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _('profile model')
        verbose_name_plural = _('profile models')
