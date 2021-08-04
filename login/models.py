from django.db import models

# Create your models here.

class Main(models.Model): 
	fname = models.CharField(max_length=15)
	lname = models.CharField(max_length=15)
	email = models.EmailField(max_length=100,default="")
	password = models.CharField(max_length=100,default="")
