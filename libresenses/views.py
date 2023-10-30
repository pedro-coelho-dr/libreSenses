from django.shortcuts import render, redirect, get_object_or_404
from .forms import (
    FilmForm, CaptionForm, AudioDescriptionForm, 
    SignLanguageForm, MediaAlternativeForm
)
from .models import Film

def index(request):
    return render(request, 'index.html', {})

def getFilm(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    captions = film.captions.all()
    context = {'film': film, 'captions': captions}
    return render(request, 'film_profile.html', context)


def add_film(request):
    if request.method == 'POST':
        film_form = FilmForm(request.POST, request.FILES)
        caption_form = CaptionForm(request.POST, request.FILES)

        if film_form.is_valid():
            film = film_form.save()

            if caption_form.is_valid():
                caption = caption_form.save(commit=False)
                caption.film = film
                caption.save()

            return redirect('film_profile', film_id=film.id)
    else:
        film_form = FilmForm()
        caption_form = CaptionForm()

    context = {
        'film_form': film_form,
        'caption_form': caption_form
    }

    return render(request, 'add_film.html', context)

def add_caption(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    form = CaptionForm(request.POST or None, request.FILES or None, initial={'film': film})
    
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('getFilm', film_id=film_id)

    context = {'form': form, 'film': film}
    return render(request, 'add_caption.html', context)

""" 
def add_audio_description(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    if request.method == 'POST':
        form = AudioDescriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('film_detail', film_id=film_id)
    else:
        form = AudioDescriptionForm(initial={'film': film})
    return render(request, 'add_audio_description.html', {'form': form, 'film': film})

def add_sign_language(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    if request.method == 'POST':
        form = SignLanguageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('film_detail', film_id=film_id)
    else:
        form = SignLanguageForm(initial={'film': film})
    return render(request, 'add_sign_language.html', {'form': form, 'film': film})

def add_media_alternative(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    if request.method == 'POST':
        form = MediaAlternativeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('film_detail', film_id=film_id)
    else:
        form = MediaAlternativeForm(initial={'film': film})
    return render(request, 'add_media_alternative.html', {'form': form, 'film': film}) """