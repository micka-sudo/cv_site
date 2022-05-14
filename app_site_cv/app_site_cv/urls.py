from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('home.urls'), name='home'),
                  path('', include('skills.urls'), name='skills'),
                  path('', include('contact.urls'), name='contact'),
                  path('', include('etudes.urls'), name='etudes'),
                  path('', include('experience.urls'), name='experiences'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
