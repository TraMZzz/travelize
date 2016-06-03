# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.gis.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from travelize.users.models import User
from travelize.product.models import Product


@python_2_unicode_compatible
class Sale(models.Model):
    user = models.ForeignKey(User, verbose_name=_('User'),
                             related_name='users')
    product = models.ForeignKey(Product, verbose_name=_('Product'),
                                related_name='product')
    amount = models.PositiveIntegerField(_('amount'))

    def __str__(self):
        return self.user.username
