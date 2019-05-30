from django.db import models
from django.urls import reverse
# Create your models here.
class newitems(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    price=models.DecimalField(decimal_places=2,max_digits=1000)

    def get_absolute_url(self):
        return reverse('classitems:itemsdetailview',kwargs={'id':self.id})