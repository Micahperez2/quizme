from django import forms
from app.models import Question

class QuestionForm(forms.Form):
    answer_choice = forms.IntegerField()

