from django.shortcuts import render
import requests
from app.models import Question
from app.forms import QuestionForm
from twilio.rest import Client 

def home(request):
    first_question = Question(question="What is the square root of 64?")
    return render(request, 'app/home.html', {'Question':first_question})

def question(request):
    first_question = Question(qnumber=1, question="What is the square root of 64?", answer1 = "8", answer2 = "16", answer3 = "4", answer4 = "32")

    # account_sid = 'AC20836d59b47c39c0ab168acbec14359a' 
    # auth_token = '' 
    # client = Client(account_sid, auth_token) 
    
    # message = client.messages.create( 
    #                             from_='+17402793165',      
    #                             body='Test Message', 
    #                             to='+19168968982' 
    #                         ) 
    
    # print(message.sid)
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        if 'one' in request.POST:
            print("one")
        elif 'two' in request.POST:
            print("two")
        elif 'three' in request.POST:
            print("three")
        elif 'four' in request.POST:
            print("four")
            
    return render(request, 'app/question.html', {'question_form': QuestionForm(), 'Question':first_question})
