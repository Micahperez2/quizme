from django.shortcuts import render, redirect
import os
import csv
from django.conf import settings
import requests
from app.models import Question, PhoneNumber, Article, FinalScore
from app.forms import QuestionForm, PhoneNumberForm
from twilio.rest import Client 


def home(request):
    file_path = os.path.join(settings.STATIC_DIR, 'articles/Article.html')
    #file_path = staticfiles_storage.url('images/Article.html')
    f = open(file_path, 'r')
    content = f.read()
    current_article = Article(body=content, date="hi")
    request.session['q_num'] = 1
    request.session['total_score'] = 0
    return render(request, 'app/home.html', {'Article':current_article})

def question(request):
    #current_question = Question(qnumber=1, correct_answer=2, question="What is the square root of 64?", answer1 = "8", answer2 = "16", answer3 = "4", answer4 = "32")
    file_path = os.path.join(settings.STATIC_DIR, 'questions/questions.csv')

    question_data = list(csv.reader(open(file_path)))

    q_num = request.session.get('q_num')
    request.session['q_num'] = q_num + 1


    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        #if (request.POST.get("val") == cor_ans):
        #    total_score += 1
        if (str(request.POST.get("val")) == str(question_data[q_num-1][1])):
            total_score = request.session.get('total_score')
            request.session['total_score'] = total_score + 1
        if (q_num != 6):
            current_question = Question(qnumber=question_data[q_num][0], correct_answer=question_data[q_num][1], question=question_data[q_num][2], answer1 = question_data[q_num][3], answer2 = question_data[q_num][4], answer3 = question_data[q_num][5], answer4 = question_data[q_num][6])
            return render(request, 'app/question.html', {'question_form': QuestionForm(), 'Question':current_question})
        else:
            return redirect('score')

    #current_question = Question(qnumber=q_num, correct_answer=cor_ans, question=quest, answer1 = ans1, answer2 = ans2, answer3 = ans3, answer4 = ans4)
    current_question = Question(qnumber=question_data[q_num][0], correct_answer=question_data[q_num][1], question=question_data[q_num][2], answer1 = question_data[q_num][3], answer2 = question_data[q_num][4], answer3 = question_data[q_num][5], answer4 = question_data[q_num][6])
    return render(request, 'app/question.html', {'question_form': QuestionForm(), 'Question':current_question})


def score(request):
    end_score = FinalScore(final_score=request.session['total_score'])
    if request.method == 'POST':
        form = PhoneNumberForm(request.POST)
        if form.is_valid():
            client_num = form.cleaned_data['phone']
            account_sid = 'AC20836d59b47c39c0ab168acbec14359a' 
            auth_token = '' 
            client = Client(account_sid, auth_token) 
            message = client.messages.create( 
                from_='+17402793165',      
                body=('Your Score: ' + str(request.session['total_score']) + "! Thank you for registering for daily updates about new topics to learn!"), 
                to=(str(client_num)),
            ) 
            phone_data_path = os.path.join(settings.DATA_DIR, 'phone.txt')
            number_in_file = 0
            with open(phone_data_path) as searchfile:
                for line in searchfile:
                    if str(client_num) in line:
                        number_in_file = 1
                        print(line)
            if number_in_file == 0:
                with open( phone_data_path, 'a') as the_file:
                    the_file.write(str(client_num) + '\n')
            #print(message.sid)
    else:
        form = PhoneNumberForm()
    return render(request, 'app/score.html', {'form': form, 'FinalScore':end_score})
