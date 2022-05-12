from django.shortcuts import render
from .models import Skills
from .forms import SkillsForm
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect
# from django.shortcuts import get_object_or_404
# from django.http import HttpResponse


def skills(request):
    skills = Skills.objects.all().order_by()
    return render(request, 'skills/skills.html', context={"skills": skills})


def create_skills(request):
    form = SkillsForm
    if request.method == 'POST':
        form = SkillsForm(request.POST, request.FILES)
        form.save()
        return HttpResponseRedirect(reverse('skills:skills'))
    return render(request, "skills:create_skills", context={'form': form})

