from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from apps.gitHub.controller import RepositoryController

# Create your views here.
class inicio(TemplateView):

    def get(self, request, *args, **kwargs):
        repos=RepositoryController.getList(self,name="",order='1')
        return render(request, 'gitHubList.html', {'name':'','repos':repos})
    
    def post(self, request, *args, **kwargs):
        name = request.POST.get('name', '')
        order = request.POST.get('ordenar', '')
        repos = RepositoryController.getList(self,name=name,order=order)
        print('---------------------------------------------')
        print(order)
        return render(request, 'gitHubList.html', {'name':name,'repos':repos, 'ordenarSel':order})

def sync(request,*args):
    repo=RepositoryController()
    res=repo.sync(p_uri='https://api.github.com/orgs/githubtraining/repos',p_token='5dc2849f045ffe8d47769ff825db547ed3c261b5')
    if res==1:
        return HttpResponseRedirect('/github')
    else:
        #msg error
        return HttpResponseRedirect('/github')
