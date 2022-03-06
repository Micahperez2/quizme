from django.shortcuts import render, redirect
import os, csv, requests
from django.conf import settings
from app.models import Question, PhoneNumber, Article, FinalScore
from app.forms import QuestionForm, PhoneNumberForm
from twilio.rest import Client 


def home(request):
    #Find path of article file and place it into model object
    file_path = os.path.join(settings.STATIC_DIR, 'articles/Article.html')
    f = open(file_path, 'r')
    content = f.read()
    current_article = Article(body=content, date="3/6/2022")

    #Create session of current question number and score
    request.session['q_num'] = 1
    request.session['total_score'] = 0
    return render(request, 'app/home.html', {'Article':current_article})

def question(request):
    #Get path of Questions from CSV file
    file_path = os.path.join(settings.STATIC_DIR, 'questions/questions.csv')
    question_data = list(csv.reader(open(file_path)))

    #Find current question user is on
    q_num = request.session.get('q_num')
    request.session['q_num'] = q_num + 1

    #If answer is submitted via post request then move on to next question
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        #If correct answer was chosen on last page then add to score
        if (str(request.POST.get("val")) == str(question_data[q_num-1][1])):
            total_score = request.session.get('total_score')
            request.session['total_score'] = total_score + 1
        if (q_num != 6):
            current_question = Question(qnumber=question_data[q_num][0], correct_answer=question_data[q_num][1], question=question_data[q_num][2], answer1 = question_data[q_num][3], answer2 = question_data[q_num][4], answer3 = question_data[q_num][5], answer4 = question_data[q_num][6])
            return render(request, 'app/question.html', {'question_form': QuestionForm(), 'Question':current_question})
        #If all questions are completed move onto score screen
        else:
            return redirect('score')

    #Default render question 1
    current_question = Question(qnumber=question_data[q_num][0], correct_answer=question_data[q_num][1], question=question_data[q_num][2], answer1 = question_data[q_num][3], answer2 = question_data[q_num][4], answer3 = question_data[q_num][5], answer4 = question_data[q_num][6])
    return render(request, 'app/question.html', {'question_form': QuestionForm(), 'Question':current_question})


def score(request):
    #Put users final score into a model
    end_score = FinalScore(final_score=request.session['total_score'])

    #If phone number information is put in, send a message to user (via twilio) about score
    if request.method == 'POST':
        form = PhoneNumberForm(request.POST)
        if form.is_valid():
            client_num = form.cleaned_data['phone']
            account_sid = 'AC20836d59b47c39c0ab168acbec14359a' 
            auth_token = '6b4b87b935d808784a15fdcf7e2f914d' 
            client = Client(account_sid, auth_token) 
            message = client.messages.create( 
                from_='+17402793165',      
                body=('Your Score: ' + str(request.session['total_score']) + "! Thank you for registering for daily updates about new topics to learn!"), 
                to=(str(client_num)),
            ) 
            phone_data_path = os.path.join(settings.DATA_DIR, 'phone.txt')
            number_in_file = 0
            #Look for phone number in number text file, if not already in then add
            with open(phone_data_path) as searchfile:
                for line in searchfile:
                    if str(client_num) in line:
                        number_in_file = 1
                        print(line)
            if number_in_file == 0:
                with open( phone_data_path, 'a') as the_file:
                    the_file.write(str(client_num) + '\n')
    else:
        form = PhoneNumberForm()
    return render(request, 'app/score.html', {'form': form, 'FinalScore':end_score})
