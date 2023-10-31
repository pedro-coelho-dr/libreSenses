from django import forms
from .models import Film, Caption, AudioDescription, SignLanguage, MediaAlternative

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'subtitle', 'year', 'length', 'rating', 'description', 'url', 'background', 'thumbnail']

class CaptionForm(forms.ModelForm):
    class Meta:
        model = Caption
        fields = ['file', 'language']
        exclude = ['film']

class AudioDescriptionForm(forms.ModelForm):
    class Meta:
        model = AudioDescription
        fields = ['url', 'language', 'isExtended', 'isOnlyAudio']
        exclude = ['film']

class SignLanguageForm(forms.ModelForm):
    class Meta:
        model = SignLanguage
        fields = ['url', 'language', 'isHardcoded']
        exclude = ['film']

class MediaAlternativeForm(forms.ModelForm):
    class Meta:
        model = MediaAlternative
        fields = ['file', 'language', 'description']
        exclude = ['film']
