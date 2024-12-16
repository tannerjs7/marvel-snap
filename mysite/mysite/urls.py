from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView


urlpatterns = [
    path('snap/', include('snap.urls')),
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='snap/cards', permanent=False))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)