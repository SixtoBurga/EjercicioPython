from django.db import models

class Repository(models.Model):
    idGitHub = models.IntegerField()
    name = models.CharField(max_length=200 ,null=True )
    description = models.CharField(max_length=200,null=True )
    url = models.URLField(null=True )
    created_at = models.DateField(null=True )
    updated_at = models.DateField(null=True )
    pushed_at = models.DateField(null=True )
