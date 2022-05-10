from django.urls import path

from . import views

app_name = "experiences"

urlpatterns = [
    path('experience', views.experience_pro, name='experiences'),
    path('creer', views.creer_view, name='creer'),
    path('<slug:slug>', views.experience_detail, name='experience')
]