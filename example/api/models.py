from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    followers = models.ManyToManyField(
        'self', related_name='followees', symmetrical=False
    )


class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts')
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)


class Photo(models.Model):
    post = models.ForeignKey(Post, related_name='photos')
    image = models.ImageField(upload_to="%Y/%m/%d")


class Person(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    gender = models.BooleanField(null=False)
    age = models.IntegerField()


class Article(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    body = models.TextField()
    author = models.ForeignKey(Person, related_name='articles')


class Image(models.Model):
    article = models.ForeignKey(Article, related_name='article')
    image = models.ImageField(upload_to='%Y/%m/%d')
    alt = models.CharField(max_length=255)
