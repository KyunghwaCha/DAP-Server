from django.db import models

# Create your models here.
class userInfo(models.Model):
    userId = models.CharField(max_length = 10)
    password = models.charField(max_length = 10)
