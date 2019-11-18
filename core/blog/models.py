from django.db import models
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    message = models.TextField(max_length=250, default="")
    
    def __str__(self):
        return self.name
    
class Entry(models.Model):
    post_id = models.AutoField(primary_key=True)
    heading = models.CharField(max_length=250, default="sample heading")
    body = models.TextField(max_length=10000, default="sample heading")
    thumbail = models.ImageField(upload_to="blog/media")
    author = models.CharField(max_length=50, default="admin")
    published_date = models.DateTimeField(default=timezone.now())
    status = models.CharField(max_length=250, default="draft") #published, draft, pending
    modified_date = models.DateTimeField(default=timezone.now())
    category = models.CharField(max_length=50, default="sample")
    tags = models.CharField(max_length=60, default="sample, sample2")
    slug = models.SlugField(max_length = 250)
    seo_description = models.TextField(max_length=250, default="sample SEO description")
    seo_robot =  models.CharField(max_length=80, default="sample SEO robot")
    
    def __str__(self):
        return self.heading    
    