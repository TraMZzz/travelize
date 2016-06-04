# -*- coding: utf-8 -*-

from rest_framework import serializers

from .models import User


class UserViewSetSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
