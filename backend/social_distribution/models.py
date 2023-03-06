from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid

# Create your models here.

class Author(models.Model):
    host = models.CharField(max_length=200)
    displayName = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    github = models.CharField(max_length=200)
    profileImage = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.displayName


class Post(models.Model):
    #image = models.ImageField(upload_to='post_images')
    title = models.CharField(max_length=200, default="No title")
    source = models.CharField(max_length=200, default="No source")
    origin = models.CharField(max_length=200, default="No origin")
    description = models.CharField(max_length=2000, default="No description")
    contentType = models.CharField(max_length=200, default="text/plain")
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    categories = models.CharField(max_length=200, default="No categories")
    count = models.IntegerField(default=0)
    comments = models.CharField(max_length=200,default="No comments")
    like = models.ManyToManyField(User, related_name='post_likes')
    #commentSrc = models.ForeignKey(Comment, on_delete=models.CASCADE, default=1)
    published = models.DateTimeField(auto_now_add=True)
    visibility = models.CharField(max_length=200, default="No visibility")
    unlisted = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comment', on_delete=models.CASCADE)
    text = models.TextField(default= "")
    post = models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE)
    #made_at = models.DateTimeField(default=timezone.now)
 
    def __str__(self):
        return f'{self.user.username} - {self.text}'


class Like(models.Model):
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE, default=1)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user} Like"
    

class UserProfile(models.Model):
    host = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    github = models.URLField(max_length=255)
    profile_image = models.URLField(max_length=255)
    password = models.CharField(max_length=255)




