from django.db import models

# Create your models here.

# Model for Article
class Article(models.Model):
    title = models.CharField(max_length=35)
    body = models.CharField(max_length=200)

# Model for individual question
class Question(models.Model):
    question = models.CharField(max_length=35)
    answer1 = models.CharField(max_length=20)
    answer2 = models.CharField(max_length=20)
    answer3 = models.CharField(max_length=20)
    answer4 = models.CharField(max_length=20)
