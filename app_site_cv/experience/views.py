from django.shortcuts import render
from .models import ExperiencePro
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .forms import ExperienceForm
from django.urls import reverse


def experience_pro(request):
    experiences = ExperiencePro.objects.all()
    return render(request, 'experience/experience.html', context={'experiences': experiences})
