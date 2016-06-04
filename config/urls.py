# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from rest_framework import routers

from travelize.users.views import UserViewSet
from travelize.address.views import AddressViewSet

router = routers.DefaultRouter()

router.register(
    r'users', UserViewSet, base_name='users',
)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api/address/(?P<jsonlatlng>.*)/$', AddressViewSet.as_view({'get': 'list'})),
    # url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name='home'),
    # url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name='about'),

    # Django Admin, use {% url 'admin:index' %}
    url(r'^admin/', include(admin.site.urls)),

    # User management
    # url(r'^users/', include('travelize.users.urls', namespace='users')),
    # url(r'^accounts/', include('allauth.urls')),

    # Your stuff: custom urls includes go here


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
