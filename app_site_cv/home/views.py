from django.shortcuts import render


def home(request):
    return render(request, 'home/home.html')


def experience_pro(request):
    return render(request, 'home/experience_pro.html')
