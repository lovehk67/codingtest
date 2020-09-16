from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    address_input = models.CharField(max_length=500, null=True, blank=True, help_text=_('입력받은 주소'))
    address_new = models.CharField(max_length=500, null=True, blank=True, help_text=_('도로명주소'))
    address_old = models.CharField(max_length=500, null=True, blank=True, help_text=_('지번주소'))
    phone = models.CharField(max_length=200, null=True, blank=True, help_text=_('전화번호'))
