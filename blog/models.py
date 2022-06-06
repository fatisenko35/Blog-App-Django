from django.db import models
from auth_.models import User
# Create your models here.

class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now=True)
    body = models.TextField()
    image_url = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    is_like = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name='likes')
    like_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)
    def __str__(self):
        return self.title


class CommentModel(models.Model):
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField(default="",null=True, blank=True)
    comment_count = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    pub_date = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    activate = models.BooleanField(default=False)
    class Meta:
        ordering = ['created_on']
    def __str__(self):
        return self.comment
