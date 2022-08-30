from platform import mac_ver
from django.db import models
from PIL import Image
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(default='default.jpeg', upload_to='home_page')

    def __str__(self):
        return f'{ self.title } zone'

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 700 or img.width > 700:
            output_size = (700, 700)
            img.thumbnail(output_size)
            img.save(self.image.path)


class PostDetails(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    group = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    code = models.TextField()
    results = models.TextField()
    
    def __str__(self):
        return self.title

class LanguagePostDetails(models.Model):
    header = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50)
    content = models.TextField()
    code = models.TextField()
    results = models.TextField()
    image = models.ImageField(default='default.jpeg', upload_to='home_page')


    def __str__(self):
        return str(self.header)

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     img = Image.open(self.image.path)
    #     if img.height > 700 or img.width > 700:
    #         output_size = (700, 700)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

