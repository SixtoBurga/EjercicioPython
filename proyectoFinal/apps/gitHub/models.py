from django.db import models
from datetime import datetime

class Repository(models.Model):
    idGitHub = models.IntegerField()
    name = models.CharField(max_length=200 ,null=True )
    description = models.CharField(max_length=200,null=True )
    url = models.URLField(null=True )
    created_at = models.DateTimeField(null=True )
    updated_at = models.DateTimeField(null=True )
    pushed_at = models.DateTimeField(null=True )
    sync_date = models.DateTimeField(default=datetime.now)
