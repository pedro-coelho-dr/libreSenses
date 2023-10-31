# Generated by Django 4.2.6 on 2023-10-31 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(blank=True, max_length=255)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('length', models.IntegerField(blank=True, null=True)),
                ('rating', models.CharField(blank=True, choices=[('Livre', 'Livre'), ('10', '10'), ('12', '12'), ('14', '14'), ('16', '16'), ('18', '18')], max_length=10, null=True)),
                ('description', models.TextField(blank=True)),
                ('url', models.URLField(blank=True)),
                ('background', models.ImageField(blank=True, upload_to='backgrounds/')),
                ('thumbnail', models.ImageField(blank=True, upload_to='thumbnails/')),
            ],
        ),
        migrations.CreateModel(
            name='SignLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('language', models.CharField(max_length=50)),
                ('isHardcoded', models.BooleanField(default=False)),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sign_languages', to='libresenses.film')),
            ],
        ),
        migrations.CreateModel(
            name='MediaAlternative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='media_alternatives/')),
                ('language', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media_alternatives', to='libresenses.film')),
            ],
        ),
        migrations.CreateModel(
            name='Caption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, upload_to='captions/')),
                ('language', models.CharField(blank=True, max_length=50)),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='captions', to='libresenses.film')),
            ],
        ),
        migrations.CreateModel(
            name='AudioDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('language', models.CharField(max_length=50)),
                ('isExtended', models.BooleanField(default=False)),
                ('isOnlyAudio', models.BooleanField(default=False)),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='audio_descriptions', to='libresenses.film')),
            ],
        ),
    ]
