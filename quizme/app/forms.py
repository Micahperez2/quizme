from django import forms
from app.models import Question
from phonenumber_field.formfields import PhoneNumberField

class QuestionForm(forms.Form):
    answer_choice = forms.IntegerField()

class PhoneNumberForm(forms.Form):
    phone = PhoneNumberField(        widget = forms.TextInput(
            attrs = {'style': 'max-width: 300px;',}
        ))
    

