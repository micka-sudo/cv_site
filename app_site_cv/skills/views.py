from django.shortcuts import render
from .models import Skills
from .forms import SkillsForm
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse


def skills(request):
    return render(request, 'skills/skills.html')


def create_skills(request):
    form =