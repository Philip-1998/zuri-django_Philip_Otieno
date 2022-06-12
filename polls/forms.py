from django import forms
from django.forms import ValidationError
from django.core import validators
from .models import Question,Choice

def check_z(value):
    if value[0].lower() != 'z':
        raise ValidationError("Please make sure the name starts with a z")

class FormName(forms.Form):
    name = forms.CharField(validators=[check_z])
    email = forms.EmailField()
    vmail = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])

    # def clean_botcatcher(self):
    #     if len(self.cleaned_data['botcatcher']) > 0:
    #         raise ValidationError("Gotcher bot")

    def clean(self):
        all_cleaned_data = super().clean()
        email = all_cleaned_data['email']
        vmail = all_cleaned_data['vmail']

        if email != vmail:
            raise ValidationError("You emails did not match")
    
    
class Create_choice(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question_text',)

class Create_new_choice(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ('choice_text',)
