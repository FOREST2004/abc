from django.db import models

# Create your models here.
class GetInforUpper14(models.Model):
    name = models.CharField(max_length=200)
    birth = models.DateTimeField()
    gentle = models.BooleanField(default=False)
    phonenumber = models.CharField(max_length=12)
    currentplace = models.CharField(max_length=300)
    declaration = models.ImageField(upload_to = "images/")
    oldpassport = models.ImageField(upload_to = "images/")
    cccd_image = models.ImageField(upload_to = "images/")
    
    def __str__(self):
	    return self.name


class GetInforLowwer14(models.Model):
    name = models.CharField(max_length=200)
    birth = models.DateTimeField()
    gentle = models.BooleanField(default=False)
    phonenumber = models.CharField(max_length=12)
    currentplace = models.CharField(max_length=300)
    decaration = models.ImageField(upload_to = "images/")
    formed_decaration = models.ImageField(upload_to = "images/")
    birth_certificate = models.ImageField(upload_to = "images/")
    representator = models.ImageField(upload_to = "images/")
    cccd_image = models.ImageField(upload_to = "images/")

    def __str__(self):
	    return self.name