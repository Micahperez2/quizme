# quizme
QuizMe is a online webapp built in Django that allows users to learn about a new topic every day and be quizzed on it. 

### User Features
- QuizMe allowers the user a clean interface to read through an article
- After reading the article, users are asked 5 basic questions and are given a score at the end
- When the quiz is finished, users have the option to put their phone number in and receive a text about their score. In the future we hope to add to this feature to notify users of each new days topic.

### Maintainer Features
- Articles and Questions are seperated from the main django code. QuizMe allows for html and csv files to be loaded in for the article and questions respectively. 
- QuizMe stores users phone numbers in a text file. It notices repeats and only allows one unique number in the file. 
- QuizMe is seperated into static files (such as images, articles, questions) and templates (for each webpage)
- 
### Installation

QuizMe requires [Python](https://www.python.org/downloads/) and [Django](https://www.djangoproject.com/download/) to run.

Install the dependencies and devDependencies and start the server.

```sh
git clone https://github.com/Micahperez2/quizme.git
cd quizme/quizme
python3 manage.py runserver
```

### Note

The ability to send text messages won't be possible by downloading QuizMe from the repo. To enable this on your own machine go to [Twilio](https://www.twilio.com/), create and account, and load your user credentials in ```quizme/quizme/app/views.py```
