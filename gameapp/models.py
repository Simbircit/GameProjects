from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='avatar.png', upload_to='images')

    def __str__(self):

        return f'{self.user.username}'


class Genre(models.Model):

    name = models.CharField(max_length=150)

    def __str__(self):

        return f'{self.name}'


class GamePage(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    description = models.TextField(max_length=5000)
    image = models.ImageField(upload_to='images')
    created = models.DateTimeField(auto_now=True)
    genre = models.ManyToManyField(Genre, through='GameGenre', null=True, blank=True)

    def __str__(self):

        return f'Game {self.name} Author {self.user.username}'


class GameGenre(models.Model):

    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    game = models.ForeignKey(GamePage, on_delete=models.CASCADE)


class GamePhoto(models.Model):

    image = models.ImageField(upload_to='images')
    game = models.ForeignKey(GamePage, on_delete=models.CASCADE)

    def __str__(self):

        return f'Game: {self.game} Image: {self.image}'


class GameFile(models.Model):

    file = models.FileField(upload_to='files')
    game = models.ForeignKey(GamePage, on_delete=models.CASCADE)

    def __str__(self):

        return f'Game: {self.game} File: {self.file}'


class Comment(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(GamePage, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f'Game: {self.game} User: {self.user.username}'
