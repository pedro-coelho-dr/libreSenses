from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('submit_film/', views.SubmitFilm.as_view(), name='submit_film'),
    path('add_caption/<int:film_id>/', views.AddCaption.as_view(), name='add_caption'),
    path('film/<int:film_id>/', views.FilmProfile.as_view(), name='film_profile'),
    path('film/update/<int:film_id>/', views.UpdateFilm.as_view(), name='update_film'),
    path('update_caption/<int:caption_id>/', views.UpdateCaption.as_view(), name='update_caption'),
    path('add_audio_description/<int:film_id>/', views.AddAudioDescription.as_view(), name='add_audio_description'),
    path('update_audio_description/<int:audio_description_id>/', views.UpdateAudioDescription.as_view(), name='update_audio_description'),
    path('add_sign_language/<int:film_id>/', views.AddSignLanguage.as_view(), name='add_sign_language'),
    path('update_sign_language/<int:sign_language_id>/', views.UpdateSignLanguage.as_view(), name='update_sign_language'),
    path('add_media_alternative/<int:film_id>/', views.AddMediaAlternative.as_view(), name='add_media_alternative'),
    path('update_media_alternative/<int:media_alternative_id>/', views.UpdateMediaAlternative.as_view(), name='update_media_alternative'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

