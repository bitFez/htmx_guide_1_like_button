from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    post_author = models.ForeignKey(User, on_delete=models.CASCADE)  # loads the USER linked to the profile from django AUTH
    post_content = models.TextField(null=True, blank=True)
    likes = models.ManyToManyField(User, blank=True, related_name="collected_votes")