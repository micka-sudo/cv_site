from django.db import models


class Contact(models.Model):
    Email = models.EmailField()
    Sujet = models.CharField(max_length=255)
    Message = models.TextField()

    def __str__(self):
        return self.email