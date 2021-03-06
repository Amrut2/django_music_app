# Generated by Django 3.2.4 on 2021-07-05 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicbeatapp', '0003_song_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pics/%y/%m/%d')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=100)),
            ],
        ),
    ]
