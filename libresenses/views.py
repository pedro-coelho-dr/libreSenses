from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest
from .models import Film, Caption, AudioDescription, SignLanguage, MediaAlternative
from .forms import (
    FilmForm, CaptionForm, AudioDescriptionForm, 
    SignLanguageForm, MediaAlternativeForm
)

# Index View
class Index(View):
    def get(self, request):
        films = Film.objects.all()
        return render(request, 'index.html', {'films': films})


# Film Profile View
class FilmProfile(View):
    def get(self, request, film_id):
        film = get_object_or_404(Film, pk=film_id)
        
        captions = film.captions.all()
        audio_descriptions = film.audio_descriptions.all()
        sign_languages = film.sign_languages.all()
        media_alternatives = film.media_alternatives.all()

        caption_form = CaptionForm(initial={'film': film})
        audio_description_form = AudioDescriptionForm(initial={'film': film})
        sign_language_form = SignLanguageForm(initial={'film': film})
        media_alternative_form = MediaAlternativeForm(initial={'film': film})

        context = {
            'film': film, 
            'captions': captions, 
            'audio_descriptions': audio_descriptions,
            'sign_languages': sign_languages,
            'media_alternatives': media_alternatives,
            'caption_form': caption_form,
            'audio_description_form': audio_description_form,
            'sign_language_form': sign_language_form,
            'media_alternative_form': media_alternative_form
        }

        return render(request, 'film_profile.html', context)

# Submit Film View

class SubmitFilm(View):
    def get(self, request):
        film_form = FilmForm()
        return render(request, 'submit_film.html', {'film_form': film_form})

    def post(self, request):
        film_form = FilmForm(request.POST, request.FILES)
        if film_form.is_valid():
            film = film_form.save()
            return redirect('film_profile', film_id=film.id)
        return render(request, 'submit_film.html', {'film_form': film_form})

# Update Film View
class UpdateFilm(View):
    def get(self, request, film_id):
        film = get_object_or_404(Film, pk=film_id)
        form = FilmForm(instance=film)
        return render(request, 'update_film.html', {'form': form})

    def post(self, request, film_id):
        film = get_object_or_404(Film, pk=film_id)
        form = FilmForm(request.POST, request.FILES, instance=film)
        if form.is_valid():
            form.save()
            return redirect('film_profile', film_id=film.id)
        return HttpResponseBadRequest("Invalid data")

# Add Caption View
class AddCaption(View):
    def post(self, request, film_id):
        film = get_object_or_404(Film, pk=film_id)
        form = CaptionForm(request.POST, request.FILES)
        if form.is_valid():
            caption = form.save(commit=False)
            caption.film = film
            caption.save()
            return redirect('film_profile', film_id=film_id)
        return redirect('film_profile', film_id=film_id)

# Update Caption View
class UpdateCaption(View):
    def get(self, request, caption_id):
        caption = get_object_or_404(Caption, pk=caption_id)
        film = caption.film
        form = CaptionForm(instance=caption)
        context = {'caption_form': form, 'film': film, 'edit_mode': True}
        return render(request, 'film_profile.html', context)

    def post(self, request, caption_id):
        caption = get_object_or_404(Caption, pk=caption_id)
        film = caption.film
        form = CaptionForm(request.POST, request.FILES, instance=caption)
        if form.is_valid():
            form.save()
            return redirect('film_profile', film_id=film.id)
        context = {'caption_form': form, 'film': film, 'edit_mode': True}
        return render(request, 'film_profile.html', context)

# Audio Description Views
class AddAudioDescription(View):
    def post(self, request, film_id):
        film = get_object_or_404(Film, pk=film_id)
        form = AudioDescriptionForm(request.POST, request.FILES)
        if form.is_valid():
            audio_description = form.save(commit=False)
            audio_description.film = film
            audio_description.save()
            return redirect('film_profile', film_id=film_id)
        return redirect('film_profile', film_id=film_id)

class UpdateAudioDescription(View):
    def get(self, request, audio_description_id):
        audio_description = get_object_or_404(AudioDescription, pk=audio_description_id)
        film = audio_description.film
        form = AudioDescriptionForm(instance=audio_description)
        context = {'audio_description_form': form, 'film': film, 'edit_mode': True}
        return render(request, 'film_profile.html', context)

    def post(self, request, audio_description_id):
        audio_description = get_object_or_404(AudioDescription, pk=audio_description_id)
        film = audio_description.film
        form = AudioDescriptionForm(request.POST, request.FILES, instance=audio_description)
        if form.is_valid():
            form.save()
            return redirect('film_profile', film_id=film.id)
        context = {'audio_description_form': form, 'film': film, 'edit_mode': True}
        return render(request, 'film_profile.html', context)

# Sign Language Views
class AddSignLanguage(View):
    def post(self, request, film_id):
        film = get_object_or_404(Film, pk=film_id)
        form = SignLanguageForm(request.POST, request.FILES)
        if form.is_valid():
            sign_language = form.save(commit=False)
            sign_language.film = film
            sign_language.save()
            return redirect('film_profile', film_id=film_id)
        return redirect('film_profile', film_id=film_id)

class UpdateSignLanguage(View):
    def get(self, request, sign_language_id):
        sign_language = get_object_or_404(SignLanguage, pk=sign_language_id)
        film = sign_language.film
        form = SignLanguageForm(instance=sign_language)
        context = {'sign_language_form': form, 'film': film, 'edit_mode': True}
        return render(request, 'film_profile.html', context)

    def post(self, request, sign_language_id):
        sign_language = get_object_or_404(SignLanguage, pk=sign_language_id)
        film = sign_language.film
        form = SignLanguageForm(request.POST, request.FILES, instance=sign_language)
        if form.is_valid():
            form.save()
            return redirect('film_profile', film_id=film.id)
        context = {'sign_language_form': form, 'film': film, 'edit_mode': True}
        return render(request, 'film_profile.html', context)

# Media Alternative Views
class AddMediaAlternative(View):
    def post(self, request, film_id):
        film = get_object_or_404(Film, pk=film_id)
        form = MediaAlternativeForm(request.POST, request.FILES)
        if form.is_valid():
            media_alternative = form.save(commit=False)
            media_alternative.film = film
            media_alternative.save()
            return redirect('film_profile', film_id=film_id)
        return redirect('film_profile', film_id=film_id)

class UpdateMediaAlternative(View):
    def get(self, request, media_alternative_id):
        media_alternative = get_object_or_404(MediaAlternative, pk=media_alternative_id)
        film = media_alternative.film
        form = MediaAlternativeForm(instance=media_alternative)
        context = {'media_alternative_form': form, 'film': film, 'edit_mode': True}
        return render(request, 'film_profile.html', context)

    def post(self, request, media_alternative_id):
        media_alternative = get_object_or_404(MediaAlternative, pk=media_alternative_id)
        film = media_alternative.film
        form = MediaAlternativeForm(request.POST, request.FILES, instance=media_alternative)
        if form.is_valid():
            form.save()
            return redirect('film_profile', film_id=film.id)
        context = {'media_alternative_form': form, 'film': film, 'edit_mode': True}
        return render(request, 'film_profile.html', context)