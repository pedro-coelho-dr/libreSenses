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
    year = models.IntegerField(validators=[MinValueValidator(1800), MaxValueValidator(datetime.date.today().year)], null=True)
    length = models.IntegerField(null=True, help_text="Duração em minutos.")
    rating = models.CharField(max_length=10, choices=RATING_CHOICES, null=True)
    description = models.TextField()
    url = models.URLField()
    background = models.ImageField(upload_to=get_upload_path, blank=True, validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif', 'bmp']), validate_file_size], help_text="Formatos: jpg, jpeg, png, gif, bmp.")
    thumbnail = models.ImageField(upload_to=get_upload_path, blank=True, validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif', 'bmp']), validate_file_size], help_text="Formatos: jpg, jpeg, png, gif, bmp.")
    permalink = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.year})" if self.year else self.title

class Caption(models.Model):
    film = models.ForeignKey(Film, related_name='captions', on_delete=models.CASCADE)
    caption_file = models.FileField(upload_to=get_upload_path, validators=[FileExtensionValidator(allowed_extensions=['srt', 'vtt']), validate_file_size], help_text="Formatos: srt ou vtt.")
    language = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.film.title} - {self.language}"

class AudioDescription(models.Model):
    film = models.ForeignKey(Film, related_name='audio_descriptions', on_delete=models.CASCADE)
    audio_url = models.URLField()
    language = models.CharField(max_length=50)
    is_extended = models.BooleanField(default=False, help_text="Adicionada ao conteúdo através de pausas no vídeo.")
    is_only_audio = models.BooleanField(default=False, help_text="Somente o áudio, sem o vídeo.")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
            audio_type = "Extended" if self.is_extended else "Standard"
            audio_type += " - Audio Only" if self.is_only_audio else " - Video"
            return f"{self.film.title} - {self.language} ({audio_type})"

class SignLanguage(models.Model):
    film = models.ForeignKey(Film, related_name='sign_languages', on_delete=models.CASCADE)
    sign_language_video_url = models.URLField()
    language = models.CharField(max_length=50)
    is_hardcoded = models.BooleanField(default=False, help_text="Deixe em branco se o vídeo da língua de sinais for separado do filme." )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
            hardcoded_status = "Hardcoded" if self.is_hardcoded else "Separate"
            return f"{self.film.title} - {self.language} ({hardcoded_status})"


class MediaAlternative(models.Model):
    film = models.ForeignKey(Film, related_name='media_alternatives', on_delete=models.CASCADE)
    alternative_file = models.FileField(upload_to=get_upload_path,validators=[validate_file_size])
    language = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
            return f"{self.film.title} - {self.language}"