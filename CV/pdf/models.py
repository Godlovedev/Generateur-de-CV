from django.db import models
from django.urls import reverse

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    competance = models.CharField(max_length=1000)
    langue = models.CharField(max_length=500)
    interet = models.CharField(max_length=500)
    objectif = models.TextField()
    experience = models.TextField()
    education = models.TextField()
    projet = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_added']

    def get_absolute_url(self):
        return reverse("download", kwargs={"id": self.id})