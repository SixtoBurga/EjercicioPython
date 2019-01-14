from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
class inicio(TemplateView):
    def get(self, request, *args, **kwargs):
        r = requests.get('https://api.github.com/orgs/githubtraining/repos')
        data = r.json()
        
        id= data[0]['id']
        name= data[0]['name']
        description= data[0]['description']
        url= data[0]['url']
        created_at= data[0]['created_at']
        updated_at= data[0]['updated_at']
        pushed_at= data[0]['pushed_at']

        print(id+'<br>' +name+'<br>' + description +'<br>' +url +'<br>' +created_at+'<br>' + updated_at+'<br>' + pushed_at)
        return HttpResponse(id+'<br>' +name+'<br>' + description +'<br>' +url +'<br>' +created_at+'<br>' + updated_at+'<br>' + pushed_at)