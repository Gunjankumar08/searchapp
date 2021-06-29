from django.db import models

class Product(models.Model):
    serialNo=models.CharField(max_length=1000, null= True)
    data=models.CharField(max_length=1000 , null = True)
