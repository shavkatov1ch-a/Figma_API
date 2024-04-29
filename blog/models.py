from django.db import models

class About(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to="about")

    def __str__(self):
        return self.content

class Video(models.Model):
    video = models.FileField(upload_to="video")


class Gallery(models.Model):
    image = models.ImageField(upload_to="gallery")



class Trening(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video = models.FileField(upload_to="trending")

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="author")

    def __str__(self):
        return self.name








