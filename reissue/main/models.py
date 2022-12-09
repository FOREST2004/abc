from django.db import models

# Create your models here.
class CCCD(models.Model):
    cccd=models.CharField(max_length=12)

    def __str__(self):
	    return self.cccd

class GetInfor(models.Model):
    cccd = models.ForeignKey(CCCD, on_delete=models.CASCADE) # <--- added
    name = models.CharField(max_length=200)
    birth = models.DateField()
    gender = models.CharField(max_length=200)
    phonenumber = models.CharField(max_length=12)
    location = models.CharField(max_length=300)
    guardian = models.CharField(max_length=200)
    queuenumber = models.IntegerField()

    def __str__(self):
	    return self.name