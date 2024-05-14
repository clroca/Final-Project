from django.db import models


class User(models.Model):
	userId = models.AutoField(primary_key=True)
	username = models.CharField(max_length=20, unique=True)
	password = models.CharField(max_length=20)

class Movie(models.Model):
	movieId = models.AutoField(primary_key=True)
	title = models.CharField(max_length=20, unique=True)
	stock = models.PositiveIntegerField()

class Checkout(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	movie = models.ForeignKey(Movie, on_delete=models.CASCADE)