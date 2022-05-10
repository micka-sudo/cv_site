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


def experience_detail(request, slug):
    experience = get_object_or_404(ExperiencePro, slug=slug)
    return render(request, 'experience/detail.html', context={"experience": experience})


def creer_view(request):
    form = ExperienceForm
    if request.method == 'POST':
        form = ExperienceForm(request.POST, request.FILES)
        form.save()
        return HttpResponseRedirect(reverse('experiences:experiences'))
    return render(request, "experience/creer.html", context={'form': form})
