from django.shortcuts import render
import requests
from app.models import Question
from app.forms import QuestionForm
from twilio.rest import Client 


def home(request):
    first_question = Question(question="What is the square root of 64?")
    return render(request, 'app/home.html', {'Question':first_question})

def question(request):
    current_question = Question(qnumber=1, correct_answer=2, question="What is the square root of 64?", answer1 = "8", answer2 = "16", answer3 = "4", answer4 = "32")

    q_num = request.session.get('q_num', 0)
    request.session['q_num'] = q_num + 1

    if (q_num >= 5):
        request.session['q_num'] = 1
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
        #if (request.POST.get("val") == cor_ans):
        #    total_score += 1
        if (q_num == 1):
            current_question = Question(qnumber=2, correct_answer=1, question="5*5", answer1 = "25", answer2 = "5", answer3 = "5", answer4 = "5")
            return render(request, 'app/question.html', {'question_form': QuestionForm(), 'Question':current_question})
        elif (q_num == 2):
            current_question = Question(qnumber=3, correct_answer=1, question="6*6", answer1 = "36", answer2 = "5", answer3 = "5", answer4 = "5")
            return render(request, 'app/question.html', {'question_form': QuestionForm(), 'Question':current_question})
        elif (q_num == 3):
            current_question = Question(qnumber=4, correct_answer=1, question="7*7", answer1 = "49", answer2 = "5", answer3 = "5", answer4 = "5")
            return render(request, 'app/question.html', {'question_form': QuestionForm(), 'Question':current_question})
        elif (q_num == 4):
            current_question = Question(qnumber=5, correct_answer=1, question="8*8", answer1 = "64", answer2 = "5", answer3 = "5", answer4 = "5")
            return render(request, 'app/question.html', {'question_form': QuestionForm(), 'Question':current_question})
        elif (q_num == 5):
            current_question = Question(qnumber=1, correct_answer=1, question="9*9", answer1 = "81", answer2 = "5", answer3 = "5", answer4 = "5")
            return render(request, 'app/question.html', {'question_form': QuestionForm(), 'Question':current_question})

    #current_question = Question(qnumber=q_num, correct_answer=cor_ans, question=quest, answer1 = ans1, answer2 = ans2, answer3 = ans3, answer4 = ans4)
    current_question = Question(qnumber=1, correct_answer=1, question="9*9", answer1 = "81", answer2 = "5", answer3 = "5", answer4 = "5")
    return render(request, 'app/question.html', {'question_form': QuestionForm(), 'Question':current_question})
