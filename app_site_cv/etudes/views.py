from django.shortcuts import render


def etudes(request):
    return render(request, 'etudes/etudes.html')
