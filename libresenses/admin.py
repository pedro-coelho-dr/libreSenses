from django.contrib import admin
from .models import Film, Caption, AudioDescription, SignLanguage, MediaAlternative
# Register your models here.
admin.site.register(Film)
admin.site.register(Caption)
admin.site.register(AudioDescription)
admin.site.register(SignLanguage)
admin.site.register(MediaAlternative)