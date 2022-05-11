from django.db import models


# Create your models here.
class ExperiencePro(models.Model):
    metier = models.CharField(max_length=150)
    societe = models.CharField(max_length=150)
    contenu = models.TextField()
    slug = models.SlugField(max_length=100)
    date_start = models.DateField()
    date_end = models.DateField()
    image = models.ImageField(default='default.jpg')

    # pour avoir le Titre sur la page
    def __str__(self):
        return self.metier

