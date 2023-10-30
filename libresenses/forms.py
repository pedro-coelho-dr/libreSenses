from django import forms
from .models import Film, Caption, AudioDescription, SignLanguage, MediaAlternative

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'subtitle', 'year', 'length', 'rating', 'description', 'url', 'background', 'thumbnail']

class CaptionForm(forms.ModelForm):
    class Meta:
        model = Caption
        fields = ['film', 'file', 'language']

class AudioDescriptionForm(forms.ModelForm):
    class Meta:
        model = AudioDescription
        fields = ['film', 'url', 'language', 'isExtended', 'isOnlyAudio']

class SignLanguageForm(forms.ModelForm):
    class Meta:
        model = SignLanguage
        fields = ['film', 'url', 'language', 'isHardcoded']

class MediaAlternativeForm(forms.ModelForm):
    class Meta:
        model = MediaAlternative
        fields = ['film', 'file', 'language', 'description']
