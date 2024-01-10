from django.db import models

# Create your models here.

class Emp(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile = models.BigIntegerField()
    address = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    salary = models.BigIntegerField()
    pimage = models.ImageField(upload_to = 'image')
    def __int__(self):
        return self.id