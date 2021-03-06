# Generated by Django 3.2 on 2021-04-22 09:31

from django.db import migrations, models
import django.db.models.deletion
import music.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300, null=True)),
                ('audio_file', models.FileField(blank=True, null=True, upload_to=music.models.new_music_save)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('band', models.CharField(blank=True, max_length=300, null=True)),
                ('music', models.ManyToManyField(blank=True, to='music.Music')),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('asin', models.CharField(blank=True, max_length=200, null=True)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=music.models.new_music_image_save)),
                ('band', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.band')),
                ('genre', models.ManyToManyField(blank=True, to='music.Genre')),
                ('label', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.label')),
                ('music', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.music')),
            ],
        ),
    ]
