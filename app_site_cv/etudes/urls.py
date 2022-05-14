from django.urls import path

from . import views

app_name = "etudes"

urlpatterns = [
    path('etudes/', views.etudes, name='etudes'),
]
