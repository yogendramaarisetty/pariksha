from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Candidate,Question,Challenge
from django.core.validators import RegexValidator
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
class UserRegisterForm(UserCreationForm) :
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email Address','id':'email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password','id':'pass'}), label ="Password",)
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Full Name','id':'name'}),label ="Username",)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Re-Enter Password','id':'re_pass'}))  
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
    fullname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Full Name'}),label="Full Name",help_text="Please enter yor fullname as per your govt. Id or college Id")
    rollnumber = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Roll Number'}),required=False,label="Roll Number",help_text='Enter you College rollnumber')
    mobile_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Mobile Number'}),label="Mobile Number",help_text='Enter Contact number')
    college = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'College'}),required=False)
    class Meta:
        model = Candidate
        help_texts = {
           'fullname':'Please enter yor fullname as per your govt. Id or college Id',
           'resume':'upload your updated resume'  
        }
        fields = ['fullname','rollnumber','mobile_number','college']

class QuestionCreateForm(forms.ModelForm):
    Description = forms.CharField(widget=forms.Textarea(attrs={'class': 'content','id':'q_description_editor'}))
    class Meta:
        model = Question
        fields = ['Level','Title','Type','Description','default_c_code',
        'default_cpp_code',
        'default_csharp_code',
        'default_java_code',
        'default_python_code']

class ContestCreationForm(forms.ModelForm):
    Description = forms.CharField(widget=forms.TextInput(attrs={'class': 'content','id':'text_editor'}))
    contest_questions = forms.CharField(required=False,widget = forms.TextInput(attrs={'id': 'selected_question_id_string','class':'hidden'}))
    Active = forms.CheckboxInput()
    class Meta:
        model = Challenge
        fields = ('Slug','Title','Description','Test_Duration','Date','College','Active','contest_questions')

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Username/Roll number', 'id': 'name'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Password',
            'id': 'pass',
        }
))