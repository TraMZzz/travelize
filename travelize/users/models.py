# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class User(AbstractUser):
    name = models.CharField(_('Name of User'), blank=True, max_length=255)
    phone = models.CharField(_('Phone'), blank=True, max_length=255)
    chat_id = models.CharField(_('Chat Id'), blank=True, max_length=255)
    message_id = models.CharField(_('Message Id'), blank=True, max_length=255)

    def __str__(self):
        return self.username
