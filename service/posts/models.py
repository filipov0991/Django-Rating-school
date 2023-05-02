from django.db import models
from django.urls import reverse
from users.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import numpy as np


class Post(models.Model):
    school_name = models.CharField(max_length=200, default='')
    country = models.CharField(max_length=200, default='KZ')
    city = models.CharField(max_length=200, default='')
    content = models.TextField()
    website = models.CharField(max_length=200, default='')
    your_email = models.EmailField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.post.id)])


class Rating(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])