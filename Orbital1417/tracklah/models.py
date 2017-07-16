from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.utils import timezone

class CharPost(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    donor = models.CharField(max_length=200)
    benef = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    text = models.TextField()
    clat = models.CharField(max_length=200, blank=True, null=True)
    clng =  models.CharField(max_length=200, blank=True, null=True)

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, null= True, blank =True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True,null= True, blank =True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        
class CharityProjects(models.Model):
    projectName= models.CharField(max_length=200, blank=True, null=True)
    charityName= models.CharField(max_length=200, blank=True, null=True)
    country= models.CharField(max_length=200, blank=True, null=True)
    lat= models.CharField(max_length=200, blank=True, null=True)
    lng= models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title