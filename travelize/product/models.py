# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.gis.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from travelize.diller.models import Diller


@python_2_unicode_compatible
class Product(models.Model):
    name = models.CharField(_('Name of User'), max_length=255),
    price = models.PositiveIntegerField(_('Price')),
    quantity = models.PositiveIntegerField(_('Quantity'))
    diller = models.ForeignKey(Diller, verbose_name=_('Diller'),
                               related_name='dillers')

    def __str__(self):
        return self.name
