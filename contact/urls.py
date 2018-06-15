from django.conf.urls import include, url
from django.urls import path, re_path
from django.contrib import admin

from .views import (
    contact,
    thanks
    )

app_name='contact'

urlpatterns = [
    path('', contact, name='contact'),
    path('thanks/', thanks, name='thanks'),
]
