from django.db import models


class Song(models.Model):
        song_id = models.AutoField(primary_key=True)
        name = models.CharField(max_length=50)
        singer = models.CharField(max_length=200)
        tags = models.CharField(max_length=100)
        image  =  models.ImageField(upload_to = 'media/images')
        song = models.FileField( upload_to = 'media/images')
        movie = models.CharField( max_length=500, default = "")

        def __str__(self):
            return self.name


class Carousel(models.Model):
    image = models.ImageField(upload_to= "pics/%y/%m/%d")
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)

    def __str__(self):
        return self.title



        