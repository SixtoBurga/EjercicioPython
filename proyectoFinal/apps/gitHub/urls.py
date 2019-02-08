from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from apps.gitHub.views import inicio
from apps.gitHub.views import sync

urlpatterns = [
    url(r'^$', inicio.as_view()),
    url(r'^sync/$', sync),
]
