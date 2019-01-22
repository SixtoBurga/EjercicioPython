from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from apps.gitHub.controller import RepositoryController

# Create your views here.
class inicio(TemplateView):
    def get(self, request, *args, **kwargs):
        RepositoryController.sync(self)
        return HttpResponse(id)