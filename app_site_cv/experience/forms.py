from django.forms import ModelForm
from .models import ExperiencePro
from django import forms


class ExperienceForm(ModelForm):
    class Meta:
        model = ExperiencePro
        fields = ['metier', 'societe', 'contenu', 'slug', 'date_start', 'date_end', 'image']







