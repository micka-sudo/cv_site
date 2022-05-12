from django.urls import path
from contact import views as contact_views
from . import views

app_name = "contact"

urlpatterns = [
    path('contact/', contact_views.contact_view, name='contact'),
    path('succes/', contact_views.contact_view, name='succes'),
]