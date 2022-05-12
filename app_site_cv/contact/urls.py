from django.urls import path
from contact import views as contact_views

app_name = "contact"

urlpatterns = [
    path('contact/', contact_views.contact_view, name='contact'),
]