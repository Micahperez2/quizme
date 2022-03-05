from django.shortcuts import render
import requests
from app.models import Question

def home(request):
    first_question = Question(question="What is the square root of 64?")
    return render(request, 'app/home.html', {'Question':first_question})
