
from apps.gitHub.models import Repository
from datetime import datetime
import requests
import pytz

class RepositoryController():
    def insert(idGitHub,name,description,url,created_at,updated_at,pushed_at):
        date_format = "%Y-%m-%dT%H:%M:%SZ"
        repo = Repository.objects.create(idGitHub = int(idGitHub))
        repo.name = name
        repo.description = description
        repo.url = url
        repo.created_at = datetime.strptime(created_at, date_format)
        repo.updated_at = datetime.strptime(updated_at, date_format)
        repo.pushed_at = datetime.strptime(pushed_at, date_format)
        repo.save()

    def update(id,name,description,url,updated_at,pushed_at):
        date_format = "%Y-%m-%dT%H:%M:%SZ"
        repo = Repository.objects.get(id=id)
        repo.name = name
        repo.description = description
        repo.url = url
        repo.updated_at = datetime.strptime(updated_at, date_format)
        repo.pushed_at = datetime.strptime(pushed_at, date_format)
        repo.sync_date  =datetime.now()
        repo.save()

    def validate(idGitHub,updated_at,pushed_at):
        # return 0: No existe el repositorio
        # return 1: Existe pero no hubo cambios
        # return 2: Existe y si hubo cambios
        date_format = "%Y-%m-%dT%H:%M:%SZ"
        res=0
        id=0
        repo = Repository.objects.filter(idGitHub=int(idGitHub))
        if repo:
            mod_updated_at = pytz.utc.localize(datetime.strptime(updated_at, date_format))

            print(mod_updated_at)
            print(repo[0].updated_at)

            if mod_updated_at>repo[0].updated_at:
                res=2
                id=repo[0].id
            else:
                res=1
        return res,id

    def sync(self, p_uri,p_token):
        r = requests.get(p_uri, headers={'Authorization': 'token '+p_token})
        data = r.json()

        if 'message' in data:
            print('Error API')
        else:
            for obj in data:
                name= obj['name']
                idGitHub=obj['id']
                description= obj['description']
                url= obj['url']
                created_at= obj['created_at']
                updated_at= obj['updated_at']
                pushed_at= obj['pushed_at']

                resultValidate, id=RepositoryController.validate(idGitHub,updated_at,pushed_at)

                if resultValidate > 0:
                    if resultValidate==2: # Existe y si hubo cambios
                        RepositoryController.update(id,name,description,url,updated_at,pushed_at)
                else:
                    RepositoryController.insert(idGitHub,name,description,url,created_at,updated_at,pushed_at)
                

    def getList(self,name):
        if name:
            repos = Repository.objects.filter(name=name)
        else:
            repos = Repository.objects.all()
        print('lista................................')
        print(repos)
        context = {'repos': repos}
        return context
