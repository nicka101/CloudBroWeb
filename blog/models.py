from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    created = models.DateTimeField('Creation date', auto_now=False, auto_now_add=True)
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title