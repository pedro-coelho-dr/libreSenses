from django.db import models

# Create your models here.
class Film(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True)
    year = models.IntegerField(blank=True, null=True)
    length = models.IntegerField(help_text="", blank=True, null=True) # minutes
    RATING_CHOICES = (
        ('Livre', 'Livre'),
        ('10', '10'),
        ('12', '12'),
        ('14', '14'),
        ('16', '16'),
        ('18', '18'),
    )
    rating = models.CharField(max_length=10, choices=RATING_CHOICES, blank=True, null=True)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)
    background = models.ImageField(upload_to='backgrounds/',blank=True)
    thumbnail = models.ImageField(upload_to='thumbnails/',blank=True)

class Caption(models.Model):
    film = models.ForeignKey(Film, related_name='captions', on_delete=models.CASCADE)
    file = models.FileField(upload_to='captions/', blank=True)
    language = models.CharField(max_length=50, blank=True)  # CHOICES

class AudioDescription(models.Model):
    film = models.ForeignKey(Film, related_name='audio_descriptions', on_delete=models.CASCADE)
    url = models.URLField()
    language = models.CharField(max_length=50)  # CHOICES
    isExtended = models.BooleanField(default=False)
    isOnlyAudio = models.BooleanField(default=False)

class SignLanguage(models.Model):
    film = models.ForeignKey(Film, related_name='sign_languages', on_delete=models.CASCADE)
    url = models.URLField()
    language = models.CharField(max_length=50)  # CHOICES
    isHardcoded = models.BooleanField(default=False)

class MediaAlternative(models.Model):
    film = models.ForeignKey(Film, related_name='media_alternatives', on_delete=models.CASCADE)
    file = models.FileField(upload_to='media_alternatives/')
    language = models.CharField(max_length=50) # CHOICES
    description = models.TextField()