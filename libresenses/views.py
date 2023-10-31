from django.shortcuts import render, redirect, get_object_or_404
from .forms import (
    FilmForm, CaptionForm, AudioDescriptionForm, 
    SignLanguageForm, MediaAlternativeForm
)

from django.http import HttpResponseBadRequest
from .models import Film, Caption, AudioDescription, SignLanguage, MediaAlternative

def index(request):
    films = Film.objects.all()
    return render(request, 'index.html', {'films': films})

# Film Profile

def getFilm(request, film_id):
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

# Film

def submit_film(request):
    if request.method == 'POST':
        film_form = FilmForm(request.POST, request.FILES)
        if film_form.is_valid():
            film = film_form.save()
            return redirect('film_profile', film_id=film.id)
    else:
        film_form = FilmForm()

    context = {'film_form': film_form}
    return render(request, 'submit_film.html', context)

def update_film(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    if request.method == "POST":
        form = FilmForm(request.POST, request.FILES, instance=film)
        if form.is_valid():
            form.save()
            return redirect('film_profile', film_id=film.id)
        else:
            return HttpResponseBadRequest("Invalid data")
    return redirect('getFilm', film_id=film.id)

# Caption

def add_caption(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    
    if request.method == 'POST':
        form = CaptionForm(request.POST, request.FILES)
        
        if form.is_valid():
            caption = form.save(commit=False)
            caption.film = film
            caption.save()
            return redirect('film_profile', film_id=film_id)
        
        return redirect('film_profile', film_id=film_id)
    
def update_caption(request, caption_id):
    caption = get_object_or_404(Caption, pk=caption_id)
    film = caption.film

    if request.method == 'POST':
        form = CaptionForm(request.POST, request.FILES, instance=caption)
        if form.is_valid():
            form.save()
            return redirect('film_profile', film_id=film.id)
    else:
        form = CaptionForm(instance=caption)

    context = {'caption_form': form, 'film': film, 'edit_mode': True}
    return render(request, 'film_profile.html', context)

#Audio Description

def add_audio_description(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    
    if request.method == 'POST':
        form = AudioDescriptionForm(request.POST, request.FILES)
        
        if form.is_valid():
            audio_description = form.save(commit=False)  
            audio_description.film = film  
            audio_description.save()  
            return redirect('film_profile', film_id=film_id)
        
        return redirect('film_profile', film_id=film_id)

def update_audio_description(request, audio_description_id):
    audio_description = get_object_or_404(AudioDescription, pk=audio_description_id)
    film = audio_description.film

    if request.method == 'POST':
        form = AudioDescriptionForm(request.POST, request.FILES, instance=audio_description)
        if form.is_valid():
            form.save()
            return redirect('film_profile', film_id=film.id)
    else:
        form = AudioDescriptionForm(instance=audio_description)

    context = {'audio_description_form': form, 'film': film, 'edit_mode': True}
    return render(request, 'film_profile.html', context)

# Sign Language

def add_sign_language(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    
    if request.method == 'POST':
        form = SignLanguageForm(request.POST, request.FILES)
        
        if form.is_valid():
            sign_language = form.save(commit=False)  
            sign_language.film = film  
            sign_language.save()  
            return redirect('film_profile', film_id=film_id)
        
        return redirect('film_profile', film_id=film_id)

def update_sign_language(request, sign_language_id):
    sign_language = get_object_or_404(SignLanguage, pk=sign_language_id)
    film = sign_language.film

    if request.method == 'POST':
        form = SignLanguageForm(request.POST, request.FILES, instance=sign_language)
        if form.is_valid():
            form.save()
            return redirect('film_profile', film_id=film.id)
    else:
        form = SignLanguageForm(instance=sign_language)

    context = {'sign_language_form': form, 'film': film, 'edit_mode': True}
    return render(request, 'film_profile.html', context)

# Media Alternative

def add_media_alternative(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    
    if request.method == 'POST':
        form = MediaAlternativeForm(request.POST, request.FILES)
        
        if form.is_valid():
            media_alternative = form.save(commit=False)  
            media_alternative.film = film  
            media_alternative.save()  
            return redirect('film_profile', film_id=film_id)
        
        return redirect('film_profile', film_id=film_id)

def update_media_alternative(request, media_alternative_id):
    media_alternative = get_object_or_404(MediaAlternative, pk=media_alternative_id)
    film = media_alternative.film

    if request.method == 'POST':
        form = MediaAlternativeForm(request.POST, request.FILES, instance=media_alternative)
        if form.is_valid():
            form.save()
            return redirect('film_profile', film_id=film.id)
    else:
        form = MediaAlternativeForm(instance=media_alternative)

    context = {'media_alternative_form': form, 'film': film, 'edit_mode': True}
    return render(request, 'film_profile.html', context)