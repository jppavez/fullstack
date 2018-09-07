from django.db import models

class Book(models.Model):
	name = models.TextField()