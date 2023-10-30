from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('add_film/', views.add_film, name='add_film'),
    path('add_caption/<int:film_id>/', views.add_caption, name='add_caption'),
    path('film/<int:film_id>/', views.getFilm, name='film_profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    
    
    
"""     path('add_audio_description/<int:film_id>/', views.add_audio_description, name='add_audio_description'),
    path('add_sign_language/<int:film_id>/', views.add_sign_language, name='add_sign_language'),
    path('add_media_alternative/<int:film_id>/', views.add_media_alternative, name='add_media_alternative'), """
