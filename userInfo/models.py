from django.db import models

# Create your models here.
class UserInfo(models.Model):
    userId = models.CharField(max_length=10,primary_key=True)
    password = models.charField(max_length=10)
    email = models.EmailField(unique=True)
    birth = models.DateField()
    gender = models.IntegerField()

class Meta:
    ordering =['created']