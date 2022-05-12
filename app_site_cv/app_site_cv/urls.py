from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'), name='home'),
    path('', include('skills.urls'), name='skills'),
    path('', include('contact.urls'), name='contact'),
    path('', include('experience.urls'), name='experiences'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
