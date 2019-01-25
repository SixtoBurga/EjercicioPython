from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from apps.gitHub.controller import RepositoryController

# Create your views here.
class inicio(TemplateView):
    def get(self, request, *args, **kwargs):
        #RepositoryController.sync(self,p_uri='https://api.github.com/orgs/githubtraining/repos',p_token='5dc2849f045ffe8d47769ff825db547ed3c261b5')
        context=RepositoryController.getList(self,name="")
        return render(request, 'gitHubList.html', context)

def sync(request,*args):
    repo=RepositoryController()
    repo.sync(p_uri='https://api.github.com/orgs/githubtraining/repos',p_token='5dc2849f045ffe8d47769ff825db547ed3c261b5')
    return HttpResponseRedirect('/github') 
