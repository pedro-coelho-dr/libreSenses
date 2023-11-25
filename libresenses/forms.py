import os
from django import forms
from .models import Film, Caption, AudioDescription, SignLanguage, MediaAlternative
from django.utils import timezone
from django.utils.text import slugify
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field
from crispy_forms.bootstrap import FormActions, InlineRadios


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = [
            'title', 'subtitle', 'year', 'length', 'rating', 
            'description', 'url', 'background', 'thumbnail', 
            'permalink'
        ]
        labels = {
            'title': 'Título da Produção',
            'subtitle': 'Subtítulo da Produção',
            'year': 'Ano da Produção',
            'length': 'Duração',
            'rating': 'Classificação Indicativa',
            'description': 'Descrição',
            'url': 'Url do Vídeo',
            'background': 'Imagem de Background',
            'thumbnail': 'Imagem para Thumbnail',
            'permalink': 'Permalink'
        }

    def __init__(self, *args, **kwargs):
        super(FilmForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].help_text = ''
        self.fields['rating'].widget = forms.RadioSelect(choices=Film.RATING_CHOICES)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='form-group col-md-6 mb-0')
            ),
            Row(
                Column('subtitle', css_class='form-group col-md-6 mb-0')
            ),
            Row(
                Column('year', css_class='form-group col-md-3 mb-0')
            ),
            Row(
                Column('length', css_class='form-group col-md-3 mb-0')
            ),
            Row(
                Column(InlineRadios('rating'), css_class='form-group col-md-8 mb-0')
            ),
            Row(
                Column('description', css_class='form-group col-md-10 mb-0')
            ),
            Row(
                Column('url', css_class='form-group col-md-6 mb-0')
            ),
            Row(
                Column('permalink', css_class='form-group col-md-6 mb-0')
            ),
            Row(
                Column('background', css_class='form-group col-md-6 mb-0')
            ),
            Row(
                Column('thumbnail', css_class='form-group col-md-6 mb-0')
            ),
            FormActions(
                Submit('submit', 'Salvar Produção', css_class='btn btn-dark btn-flat')
            )
        )
        self.fields['title'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite o título do filme'
        })
        self.fields['subtitle'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite o subtítulo do filme'
        })
        self.fields['year'].widget = forms.NumberInput(attrs={
            'class': 'form-control',
            'min': 1850,
            'max': 2100,
            'placeholder': 'Digite o ano'
        })
        self.fields['length'].widget = forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite a duração do filme em minutos'
        })
        self.fields['description'].widget = forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Digite a descrição do filme'
        })
        self.fields['url'].widget = forms.URLInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite a URL do filme'
        })
        self.fields['background'].widget = forms.ClearableFileInput(attrs={
            'class': 'form-control',
            'accept': 'image/*',
            'placeholder': 'Escolha a imagem de fundo'
        })
        self.fields['thumbnail'].widget = forms.ClearableFileInput(attrs={
            'class': 'form-control',
            'accept': 'image/*',
            'placeholder': 'Escolha a miniatura'
        })
        self.fields['permalink'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite o link permanente'
        })
                
        @staticmethod
        def validate_image_file_size(value):
            max_size_mb = 2
            if value.size > max_size_mb * 1024 * 1024:
                raise forms.ValidationError(f"O tamanho máximo do arquivo que pode ser carregado é de {max_size_mb} MB")

        def clean_background(self):
            background = self.cleaned_data.get('background', False)
            if background:
                self.validate_image_file_size(background)
                if not background.name.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
                    raise forms.ValidationError("Formato de arquivo não suportado. Por favor, carregue uma imagem nos formatos JPG, JPEG, PNG, GIF ou BMP.")
            return background

        def clean_thumbnail(self):
            thumbnail = self.cleaned_data.get('thumbnail', False)
            if thumbnail:
                self.validate_image_file_size(thumbnail)
                if not thumbnail.name.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
                    raise forms.ValidationError("Formato de arquivo não suportado. Por favor, carregue uma imagem nos formatos JPG, JPEG, PNG, GIF ou BMP.")
            return thumbnail
        
        
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
