from django import forms
from app.models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('answer1', 'answer2', 'answer3', 'answer4' )
