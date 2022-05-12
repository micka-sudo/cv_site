from django.db import models

# Create your models here.


class Skills(models.Model):
    titre = models.CharField(max_length=15)
    niveau = models.IntegerField(max_length=3)
