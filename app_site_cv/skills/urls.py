from django.urls import path

from . import views

app_name = "skills"

urlpatterns = [
    path('skills/', views.skills, name='skills'),
    path('create_skills', views.create_skills, name='create_skills')
]
