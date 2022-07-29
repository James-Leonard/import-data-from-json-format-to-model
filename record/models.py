from django.db import models

class Details(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phone=models.IntegerField()
    rating=models.IntegerField()
    review=models.CharField(max_length=200)
    description=models.CharField(max_length=300)

