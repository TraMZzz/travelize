# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json

from django.contrib.gis.geos import GEOSGeometry

from rest_framework.response import Response
from rest_framework import (
    exceptions, filters, mixins, pagination,
    permissions, serializers, status, viewsets)

from .models import Address


class AddressViewSet(viewsets.GenericViewSet):

    def list(self, request, jsonlatlng):
        point = GEOSGeometry('{ "type": "Point", "coordinates": ['+jsonlatlng+']}')
        all_address = Address.objects.distance(point).order_by('distance')[:5]
        data = {}
        for address in all_address:
            dillers = address.addresses.all().order_by('product_dillers__price')[:1]
            if dillers:
                diller = dillers[0]
                product = diller.product_dillers.all().order_by('price')[0]
                data[diller.id] = {'location': address.location.tuple,
                                   'price': product.price,
                                   'product': product.product_name,
                                   'name': diller.name,
                                   'phone': diller.phone}
        return Response(status=200, data=data)
