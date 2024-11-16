from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.beranda, name='beranda'),
    path('tentang-kami/', views.tentangkami, name='tentangkami'),
    path('layanan/', views.layanan, name='layanan'),
    path('galeri/', views.galeri, name='galeri')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)