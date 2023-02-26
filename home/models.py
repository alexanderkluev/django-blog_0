from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Tag(models.Model):
    tag_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.tag_name

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    img_url = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    text = models.CharField(max_length=400)
    published_date = models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        return self.text[:10] + '...'






