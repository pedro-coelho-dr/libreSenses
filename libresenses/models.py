from django.db import models
from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator
import datetime

from django.forms import ValidationError


def validate_file_size(value):
    max_size_mb = 2
    if value.size > max_size_mb * 1024 * 1024:
        raise ValidationError(f"O tamanho máximo do arquivo que pode ser carregado é de {max_size_mb} MB")

def get_upload_path(instance, filename):
    if isinstance(instance, Film):
        return f'{instance.permalink}/{filename}'
    else:
        return f'{instance.film.permalink}/{filename}'

#LEMBRAR DE REAVALIAR OS BLANK=TRUE
class Film(models.Model):
    RATING_CHOICES = (
        ('Livre', 'Livre'),
        ('10', '10'),
        ('12', '12'),
        ('14', '14'),
        ('16', '16'),
        ('18', '18'),
    )
    title = models.CharField(max_length=255, db_index=True)
    subtitle = models.CharField(max_length=255, blank=True)
    year = models.IntegerField(validators=[MinValueValidator(1800), MaxValueValidator(datetime.date.today().year)], blank=True, null=True, help_text="Insira o ano de lançamento do filme.")
    length = models.IntegerField(blank=True, null=True, help_text="Duração do filme em minutos.")
    rating = models.CharField(max_length=10, choices=RATING_CHOICES, blank=True, null=True)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)
    background = models.ImageField(upload_to=get_upload_path, blank=True, validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif', 'bmp']), validate_file_size], help_text="Faça o upload da imagem de fundo nos formatos jpg, jpeg, png, gif ou bmp. Max 2MB.")
    thumbnail = models.ImageField(upload_to=get_upload_path, blank=True, validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif', 'bmp']), validate_file_size], help_text="Faça o upload da imagem em miniatura nos formatos jpg, jpeg, png, gif ou bmp. Max 2MB.")
    permalink = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.year})" if self.year else self.title

class Caption(models.Model):
    film = models.ForeignKey(Film, related_name='captions', on_delete=models.CASCADE)
    caption_file = models.FileField(upload_to=get_upload_path, blank=True, validators=[FileExtensionValidator(allowed_extensions=['srt', 'vtt']), validate_file_size], help_text="Faça o upload do arquivo de legenda nos formatos srt ou vtt. Max 2MB.")
    language = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.film.title} - {self.language.name}"

class AudioDescription(models.Model):
    film = models.ForeignKey(Film, related_name='audio_descriptions', on_delete=models.CASCADE)
    audio_url = models.URLField(help_text="URL para a descrição em áudio.")
    language = models.CharField(max_length=50)
    is_extended = models.BooleanField(default=False)
    is_only_audio = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
            audio_type = "Extended" if self.is_extended else "Standard"
            audio_type += " - Audio Only" if self.is_only_audio else " - Video"
            return f"{self.film.title} - {self.language.name} ({audio_type})"

class SignLanguage(models.Model):
    film = models.ForeignKey(Film, related_name='sign_languages', on_delete=models.CASCADE)
    sign_language_video_url = models.URLField(help_text="URL para o vídeo em língua de sinais.")
    language = models.CharField(max_length=50)
    is_hardcoded = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
            hardcoded_status = "Hardcoded" if self.is_hardcoded else "Separate"
            return f"{self.film.title} - {self.language.name} ({hardcoded_status})"


class MediaAlternative(models.Model):
    film = models.ForeignKey(Film, related_name='media_alternatives', on_delete=models.CASCADE)
    alternative_file = models.FileField(upload_to=get_upload_path,validators=[validate_file_size], help_text="Faça o upload do arquivo de mídia alternativa. Max 2MB.")
    language = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
            return f"{self.film.title} - {self.language.name}"