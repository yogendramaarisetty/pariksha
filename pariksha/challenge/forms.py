from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Candidate,Question
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
class UserRegisterForm(UserCreationForm) :
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput, label ="Password")
    username = forms.CharField(label="Rollnumber")
        
    class Meta:
        model = User
        help_texts = {
            'username': None,
            'email': None,
            'password1':None,
        }
        fields = ['username','email','password1','password2']
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'User with this Email Id already Registered')
        return email
class CandidateDetailsForm(forms.ModelForm):
    fullname = forms.CharField(label="Full Name",help_text="Please enter yor fullname as per your govt. Id or college Id")
    rollnumber = forms.CharField(required=False,label="Roll Number",help_text='Enter you College rollnumber')
    college = forms.CharField(label="College",help_text='Enter College/University Name')
    branch = forms.CharField(label="Branch",help_text='Enter your current branch CSE/ECE/MECH/...etc')
    graduation_year = forms.CharField(label="Graduation year",help_text='passed/passing out year')
    mobile_number = forms.CharField(label="Mobile Number",help_text='Enter Contact number')
    resume = forms.FileField(required=False,help_text="upload your updated resume")
    class Meta:
        model = Candidate
        help_texts = {
           'fullname':'Please enter yor fullname as per your govt. Id or college Id',
           'resume':'upload your updated resume'  
        }
        fields = ['fullname','rollnumber','college','branch','graduation_year','mobile_number']
class QuestionCreateForm(forms.ModelForm):
    Description = forms.CharField(widget=forms.TextInput(attrs={'class': 'content','id':'text_editor'}))
    class Meta:
        model = Question
        fields = ('Slug','Title','Type','Description','challenge','sample_inputs','sample_outputs','default_c_code',
        'default_cpp_code',
        'default_csharp_code',
        'default_java_code',
        'default_python_code')
    