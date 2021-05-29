from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=1024)
    content = models.CharField(max_length=4096)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    reg_date = models.DateTimeField(auto_created=True, auto_now=True)