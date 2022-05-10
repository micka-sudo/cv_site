from django.urls import path

from . import views

app_name = "experiences"

urlpatterns = [
    path('experience', views.experience_pro, name='experiences'),
    path('<slug:slug>', views.experience_pro, name='experience')
]