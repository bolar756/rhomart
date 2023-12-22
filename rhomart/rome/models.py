from django.db import models
import time
# Create your models here.

class Register(models.Model):
    Date = models.CharField(default=time.ctime(),max_length=40)
    category = models.CharField(default='category',max_length=20)
    amount=models.FloatField()
    age = models.IntegerField()
    name = models.CharField(default=time.ctime(),max_length=20)
    gender=models.CharField(default='alien',max_length=20)

    def __repr__(self):
        return self.name