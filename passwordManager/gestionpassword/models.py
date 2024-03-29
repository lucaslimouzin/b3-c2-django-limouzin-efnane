from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class SiteInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    site_name = models.CharField(max_length=100)
    site_url = models.URLField(max_length=200)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.site_name
    
    def get_delete_url(self):
        return reverse('delete_site', args=[str(self.pk)])
