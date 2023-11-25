from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('submit_film/', views.SubmitFilm.as_view(), name='submit_film'),
    path('film_list/', views.FilmList.as_view(), name='film_list'),
    path('film/<int:film_id>/', views.FilmProfile.as_view(), name='film_profile'),
    path('film/update/<int:film_id>/', views.UpdateFilm.as_view(), name='update_film'),
    path('add_caption/<int:film_id>/', views.AddCaption.as_view(), name='add_caption'),
    path('add_audio_description/<int:film_id>/', views.AddAudioDescription.as_view(), name='add_audio_description'),
    path('add_sign_language/<int:film_id>/', views.AddSignLanguage.as_view(), name='add_sign_language'),
    path('add_media_alternative/<int:film_id>/', views.AddMediaAlternative.as_view(), name='add_media_alternative'),
    path('delete/<str:model_name>/<int:entry_id>/', views.DeleteEntry.as_view(), name='delete_entry'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

