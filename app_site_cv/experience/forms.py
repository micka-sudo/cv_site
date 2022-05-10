from django.forms import ModelForm
from .models import ExperiencePro


class ExperienceForm(ModelForm):
    class Meta:
        model = ExperiencePro
        fields = ['titre', 'contenu', 'slug', 'date_start', 'date_end', 'image']
