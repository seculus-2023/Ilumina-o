from django.urls import path 
from pages import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'), 
    path('login/', views.login_view, name='login'),
    path('mapa/', views.mapa_view, name='mapa'),
    path('latitude/', views.latitude_view, name='latitude'),
    path('qrcode/', views.qrcode_view, name='qrcode'),
    path('registrar_poste/', views.registrar_poste, name='registrar_poste'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
