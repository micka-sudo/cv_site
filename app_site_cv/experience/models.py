from django.db import models


# Create your models here.
class ExperiencePro(models.Model):
    titre = models.CharField(max_length=150)
    contenu = models.TextField()
    slug = models.SlugField(max_length=100)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    image = models.ImageField(default='default.jpg')

    # pour avoir le Titre sur la page
    def __str__(self):
        return self.titre