from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

# Model for Article
class Article(models.Model):
    body = models.TextField(max_length=5000)
    date = models.CharField(max_length=20)

# Model for individual question
class Question(models.Model):
    qnumber = models.IntegerField(default=1)
    correct_answer = models.IntegerField(default=1)
    question = models.CharField(max_length=35)
    answer1 = models.CharField(max_length=20)
    answer2 = models.CharField(max_length=20)
    answer3 = models.CharField(max_length=20)
    answer4 = models.CharField(max_length=20)

#Model for phone number field
class PhoneNumber(models.Model):
    phone = PhoneNumberField(null=False, blank=True, unique=True)

#Model to hold the users final score
class FinalScore(models.Model):
    final_score = models.IntegerField(default=0)
