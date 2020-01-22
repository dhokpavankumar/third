from django.db import models
from django.urls import reverse


class Beer(models.Model):
    name=models.CharField(max_length=100)
    taste=models.CharField(max_length=100)
    color=models.CharField(max_length=100)
    price=models.FloatField()
    date=models.DateField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk':self.pk})

