from django.db import models

from django.urls import reverse
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=25)
    phone_number = models.PositiveIntegerField()
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name + " - " + str(self.phone_number)
    
    def get_absolute_url(self):
        return reverse('home')


