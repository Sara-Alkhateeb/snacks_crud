from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
class Snack(models.Model):
    name = models.CharField(max_length=255)
    description  = models.TextField(default='Snack description ')
    purchaser= models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
            return self.name
    
    def get_absolute_url(self):
        return reverse('snacksList')


