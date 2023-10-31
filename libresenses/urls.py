from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('submit_film/', views.submit_film, name='submit_film'),  # Changed URL pattern here
    path('add_caption/<int:film_id>/', views.add_caption, name='add_caption'),
    path('film/<int:film_id>/', views.getFilm, name='film_profile'),
    path('film/update/<int:film_id>/', views.update_film, name='update_film'),
    path('update_caption/<int:caption_id>/', views.update_caption, name='update_caption'),
    path('add_audio_description/<int:film_id>/', views.add_audio_description, name='add_audio_description'),
    path('update_audio_description/<int:audio_description_id>/', views.update_audio_description, name='update_audio_description'),
    path('add_sign_language/<int:film_id>/', views.add_sign_language, name='add_sign_language'),
    path('update_sign_language/<int:sign_language_id>/', views.update_sign_language, name='update_sign_language'),
    path('add_media_alternative/<int:film_id>/', views.add_media_alternative, name='add_media_alternative'),
    path('update_media_alternative/<int:media_alternative_id>/', views.update_media_alternative, name='update_media_alternative'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
