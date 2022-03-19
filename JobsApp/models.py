from django.db import models

# Create your models here.

class Jobs(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    status = models.CharField(max_length=10)
    posted_on = models.DateField()
    posted_by = models.CharField(max_length=100)