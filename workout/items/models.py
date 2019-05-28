from django.db import models
from django.urls import reverse
# Create your models here.
class item(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField(blank=True,null=True)
    price=models.DecimalField(decimal_places=2,max_digits=1000)

    def get_absolute_url(self):
        return reverse('single',kwargs={'id':self.id})
