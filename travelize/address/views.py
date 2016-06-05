# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json

from django.contrib.gis.geos import GEOSGeometry
from django.conf import settings

from rest_framework.response import Response
from rest_framework import (
    exceptions, filters, mixins, pagination,
    permissions, serializers, status, viewsets)

from .models import Address


import urllib2
from datetime import datetime, timedelta
import random

AERO_TOKEN = '17f8e412bd148d7dc81aee0ed8b7fbea'
PAYOUTS_TOKEN = '64f4f34d117155576c02558168b0f5c1'


def get_latest_prices(from_airport, to_airport, depart_date, return_date, PAYOUTS_TOKEN):
    url = 'http://api.travelpayouts.com/v1/prices/cheap?currency=USD&origin=%s&destination=%s&depart_date=%s&return_date=%s&token=%s' % (from_airport, to_airport, depart_date, return_date, PAYOUTS_TOKEN)
    print url, '!!!'
    data = urllib2.urlopen(url)
    data = data.read()
    data = json.loads(data)

    print data, '!@@@@@@@@@@@'

    return str(random.randint(0, 300))


def get_closest_airport(lat, lang, AERO_TOKEN):
    url = "https://airport.api.aero/airport/nearest/%s/%s?user_key=%s" % (lat, lang, AERO_TOKEN)
    data = urllib2.urlopen(url)
    data = data.read()
    data = data[9:-1]
    data = json.loads(data)
    return data['airports'][0]['code']


class AddressViewSet(viewsets.GenericViewSet):

    def list(self, request, jsonlatlng):
        lat, lang = jsonlatlng.split(',')
        from_airport = get_closest_airport(lat, lang, AERO_TOKEN)  # 'LWO'
        depart_date = datetime.now().strftime('%Y-%m')
        return_date = (datetime.now() + timedelta(days=2)).strftime('%Y-%m')

        point = GEOSGeometry('{ "type": "Point", "coordinates": ['+jsonlatlng+']}')
        all_address = Address.objects.distance(point).order_by('distance')[:5]
        data = {}
        count = 0
        for address in all_address:
            dillers = address.addresses.all().order_by('product_dillers__price')[:1]
            if dillers:
                diller = dillers[0]
                air_price = get_latest_prices(from_airport, diller.airport, depart_date, return_date, PAYOUTS_TOKEN)
                product = diller.product_dillers.all().order_by('price')[0]
                data[count] = {'location': address.location.tuple,
                                   'price': product.price,
                                   'product': product.product_name,
                                   'name': diller.name,
                                   'phone': diller.phone,
                                   'ticket_price': air_price,
                                   'image_url': 'http://188.226.182.203:4567'+settings.MEDIA_URL + diller.image.name}
            count += 1
        print data
        return Response(status=200, data=data)
