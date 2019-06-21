
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    university = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    dob = models.DateField()
    profile_image = models.ImageField()

    def get_absolute_url(self):
        return reverse('login')

    def __str__(self):
        return self.university
