import os
from django import forms
from .models import Film, Caption, AudioDescription, SignLanguage, MediaAlternative
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from django.utils.text import slugify


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = [
            'title', 'subtitle', 'year', 'length', 'rating', 
            'description', 'url', 'background', 'thumbnail', 
            'permalink'
        ]

    def clean_title(self):
        title = self.cleaned_data['title'].strip()
        if not title:
            raise forms.ValidationError("O título não pode ser vazio ou consistir apenas de espaços em branco.")
        return title

    def clean_subtitle(self):
        subtitle = self.cleaned_data.get('subtitle', '').strip()
        return subtitle

    def clean_year(self):
        year = self.cleaned_data['year']
        if year is None:
            return year
        current_year = timezone.now().year
        if year < 1850 or year > current_year:
            raise forms.ValidationError("Insira um ano entre 1850 e o ano atual.")
        return year

    def clean_permalink(self):
        permalink = self.cleaned_data['permalink']
        return slugify(permalink, allow_unicode=False)

class CaptionForm(forms.ModelForm):
    class Meta:
        model = Caption
        fields = ['caption_file', 'language']
        exclude = ['film', 'created_at', 'updated_at']
        
    def clean_caption_file(self):
        caption_file = self.cleaned_data.get('caption_file')
        if caption_file:
            valid_extensions = ['.srt', '.vtt']
            extension = os.path.splitext(caption_file.name)[1]
            if extension.lower() not in valid_extensions:
                raise forms.ValidationError('Arquivo de legenda deve ser nos formatos srt ou vtt.')
        return caption_file

class AudioDescriptionForm(forms.ModelForm):
    class Meta:
        model = AudioDescription
        fields = ['audio_url', 'language', 'is_extended', 'is_only_audio']
        exclude = ['film', 'created_at', 'updated_at']

class SignLanguageForm(forms.ModelForm):
    class Meta:
        model = SignLanguage
        fields = ['sign_language_video_url', 'language', 'is_hardcoded']
        exclude = ['film', 'created_at', 'updated_at']

class MediaAlternativeForm(forms.ModelForm):
    class Meta:
        model = MediaAlternative
        fields = ['alternative_file', 'language', 'description']
        exclude = ['film', 'created_at', 'updated_at']
