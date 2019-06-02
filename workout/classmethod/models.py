from django.db import models

# Create your models here.
class productname(models.Model):
    title=models.CharField(max_length=50)
    price=models.DecimalField(decimal_places=2,max_digits=1000)
