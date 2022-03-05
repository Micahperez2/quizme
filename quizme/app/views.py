from django.shortcuts import render
import requests
from app.models import Question
from twilio.rest import Client 

def home(request):
    first_question = Question(question="What is the square root of 64?")
    return render(request, 'app/home.html', {'Question':first_question})

def question(request):
    first_question = Question(question="What is the square root of 64?")

    # account_sid = 'AC20836d59b47c39c0ab168acbec14359a' 
    # auth_token = '2402f169de5756d45d5734131765f440' 
    # client = Client(account_sid, auth_token) 
    
    # message = client.messages.create( 
    #                             from_='+17402793165',      
    #                             body='Test Message', 
    #                             to='+19168968982' 
    #                         ) 
    
    # print(message.sid)
    
    return render(request, 'app/question.html', {'Question':first_question})
