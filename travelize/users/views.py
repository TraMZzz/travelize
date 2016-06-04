# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json

from django.shortcuts import get_object_or_404

from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework import (
    exceptions, filters, mixins, pagination,
    permissions, serializers, status, viewsets)


from .models import User
from .serializers import UserViewSetSerializer


class UserViewSet(viewsets.ModelViewSet):
    model = User
    serializer_class = UserViewSetSerializer

    def get_queryset(self):
        return self.model.objects.all()

    @list_route(methods=['post'])
    def add(self, request, format=None):
        data = request.data

        password = User.objects.make_random_password()
        user = User.objects.create_user(username=data.get('username'), password=password)
        return Response(status=202, data={'id': user.id})

    @detail_route(methods=['post'])
    def update(self, request, pk):
        data = request.data
        return Response(status=204)
