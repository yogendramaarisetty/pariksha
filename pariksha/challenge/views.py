from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import UserRegisterForm,CandidateDetailsForm,QuestionCreateForm,ContestCreationForm
from .models import Candidate,Challenge,Question,Candidate_codes,Testcase,challenge_questions,Question_Testcase
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from datetime import datetime,timedelta
from django.http import HttpRequest
from django.views.generic import CreateView,FormView,UpdateView,DeleteView
from django.contrib.auth import authenticate
from . tokens import account_activation_token
from django.http import HttpRequest
from django.http import HttpResponse
import json,time
import smtplib
from django.db.models import Q
from django.utils import timezone
from .coderun_api import compile_run
from django.core.mail import EmailMessage
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import login
from .forms import UserLoginForm

def temp_testpage_design(request):
    return render(request, 'challenge/testpage.html')

def pariksha_register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            rollnumber = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password1')
            user = User.objects.all().filter(username=rollnumber).first()
            form.is_active = False
            current_site = get_current_site(request)
            print(current_site)
            subject = 'Activate Your your test'          
            messages.success(request, f'Your test registration Link is sent to {email}.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'challenge/register.html',
    {'form':form},)





@user_passes_test(lambda u: u.is_superuser)
def question_view(request,q_id):
    print(q_id)


@user_passes_test(lambda u: u.is_superuser)
def question_bank(request):
    if request.method == "POST":
            form= QuestionCreateForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, f'Question is added successfully')
                return redirect('question_bank')
            else:
                return render(request,'challenge/question_bank.html',
                                {'form':form,
                                'errors':form.errors,
                                'questions':Question.objects.all()
                                }
                                )

    else:
        form= QuestionCreateForm()
        return render(request,'challenge/question_bank.html',
                                {'form':form,
                                'questions':Question.objects.all()
                                }
                                )
@user_passes_test(lambda u: u.is_superuser)
def admin_management(request):
   
    return render(request,'challenge/admin_manage.html',{'challenges': Question.objects.all(), 'test_count' : test_count})

def home(request):
    if request.user.is_authenticated:
        return redirect('tests')
    return render(request,'challenge/home.html',{
'header':'Pariksha',
'title':'Pariksha',
})


def challenges(request):
    test_count = Challenge.objects.all().count()
    print('\n\n\n\n',test_count,'\n\n\n')
    context ={
        'challenges':Challenge.objects.all(),
        'test_count': test_count
    }
    return render(request,'challenge/challenges.html',context)


@user_passes_test(lambda u: u.is_superuser)
def create_contest_form(request):
    if request.method == "POST":
        form = ContestCreationForm(request.POST)
        print('form is post',request.POST)
        data = request.POST
        contest = Challenge()
        current_contest_id = None
        if request.is_ajax():
            if request.POST.get('contest')=='yes':
                # csrf = request.POST.get('csrfmiddlewaretoken')
                # Title = request.POST.get('Title')
                # Slug = request.POST.get('Slug')
                # Duration = request.POST.get('Duration')
                # Description = request.POST.get('Description')
                # Date = request.POST.get('Date')
                Active = request.POST.get('Active')
                # College = request.POST.get('College')
                if form.is_valid():
                    print(Active)
                    activation_bool = True
                    if(Active == 'true'):
                        activation_bool = True
                    else:
                        activation_bool = False
                    form.instance.Active = activation_bool
                    form.save()
                    contest = form.save(commit=False)
                    res = {'saved':'yes',
                            'msg':'Contest Saved successfully',
                            'contest_id': contest.pk}
                    return HttpResponse(json.dumps(res), content_type="application/json")
                else:
                    return HttpResponse(json.dumps({'errors':'yes','form_errors':form.errors}), content_type="application/json")
            elif request.POST.get('challenge_question') == "yes":
                question_list = data.getlist('list[]')
                contest_id = data.get('contest_id')
                print('CURRENT_CONTEST_ID = ',contest_id) 
                for i in question_list:
                    q = Question.objects.all().get(pk = int(i))
                    c = Challenge.objects.all().get(pk = contest_id)
                    c_q = challenge_questions(challenge = c,question = q)
                    c_q.save()
                res = {'msg':'Successflly got list'}
                return HttpResponse(json.dumps(res), content_type="application/json")


            # return HttpResponse(json.dumps(res), content_type="application/json")
        else:
            return HttpResponse(json.dumps(form.errors), content_type="application/json")      

    else:
        form = ContestCreationForm()
    return render(request,'challenge/contest_create_form.html',{'form':form,'model_name':'Contest','question_bank':Question.objects.all()})

@user_passes_test(lambda u: u.is_superuser)
def manage_contests(request):
    if request.method == "POST":
        if request.is_ajax():
            contest_id = request.POST.get('contest_id')
            contest = Challenge.objects.get(pk = contest_id)
            title = contest.Title
            contest.delete()
            res = {
                'msg' : title+f' (id={contest_id}) deleted successfully'
            }
            return HttpResponse(json.dumps(res), content_type="application/json")
    test_count = Challenge.objects.all().count()
    print('\n\n\n\n',test_count,'\n\n\n')
    context ={
        'challenges':Challenge.objects.all(),
        'test_count': test_count
    }
    return render(request,'challenge/contest_management.html',context)

@user_passes_test(lambda u: u.is_superuser)
def contest_edit_form(request, contest_id):
    contest = Challenge.objects.all().get(pk = contest_id)
    if request.method == "POST":
        data = request.POST
        form = ContestCreationForm(request.POST,instance = contest)
        if request.is_ajax():
            if request.POST.get('contest')=='yes':
                Active = request.POST.get('Active')
                if form.is_valid():
                        print(Active)
                        activation_bool = True
                        if(Active == 'true'):
                            activation_bool = True
                        else:
                            activation_bool = False
                        form.instance.Active = activation_bool
                        form.save()
                        res = {'saved':'yes',
                            'msg':'Contest Updated successfully',
                            'contest_id': contest.pk}
                        return HttpResponse(json.dumps(res), content_type="application/json")
                else:
                    return HttpResponse(json.dumps({'errors':'yes','form_errors':form.errors}), content_type="application/json")
            elif request.POST.get('challenge_question') == "yes":
                new_question_list = data.getlist('new_question_list[]')
                removed_question_list = data.getlist('removed_question_list[]')
                contest_id = contest.id
                print('CURRENT_CONTEST_ID = ',contest_id) 
                for i in removed_question_list:
                    c_q = challenge_questions.objects.all().get(pk=int(i))
                    c_q.delete()
                for i in new_question_list:
                    q = Question.objects.all().get(pk = int(i))
                    c_q = challenge_questions(challenge = contest,question = q)
                    c_q.save()
                res = {'success':'yes','msg':'Successflly updated the contest questions list'}
                
                return HttpResponse(json.dumps(res), content_type="application/json")
            


            # return HttpResponse(json.dumps(res), content_type="application/json")
        else:
            return HttpResponse(json.dumps(form.errors), content_type="application/json")
    else:
        form = ContestCreationForm(instance = contest)
        this_contest_questions = challenge_questions.objects.filter(challenge = contest)
        return render(request,'challenge/contest_edit_form.html',{'form':form,'contest_id':contest.id,'model_name':'Contest','question_bank':Question.objects.all(),'contest_questions':this_contest_questions})



@user_passes_test(lambda u: u.is_superuser)
def question_bank(request):
    if request.method == "POST":
        if request.is_ajax():
            question_id = request.POST.get('question_id')
            question = Question.objects.get(pk = question_id)
            title = question.Title
            question.delete()
            res = {
                'msg' : title+f' (id={question_id}) deleted successfully'
            }
            return HttpResponse(json.dumps(res), content_type="application/json")
    question_count = Question.objects.all().count()
    context ={
        'questions':Question.objects.all(),
        'question_count': question_count
    }
    return render(request,'challenge/question_bank.html',context)

@user_passes_test(lambda u: u.is_superuser)
def create_question_form(request):
    if request.method == "POST":
        form = QuestionCreateForm(request.POST)
        data = request.POST
        question = Question()
        current_question_id = None
        if request.is_ajax():
            if request.POST.get('question')=='yes':
                if form.is_valid():
                    form.save()
                    question = form.save(commit=False)
                    res = {'saved':'yes',
                            'msg':'Question Saved successfully',
                            'question_id': question.pk
                            }
                    print('question form saved successfully')
                    return HttpResponse(json.dumps(res), content_type="application/json")
                else:
                    return HttpResponse(json.dumps({'errors':'yes','form_errors':form.errors}), content_type="application/json")
            elif request.POST.get('question_testcase') == "yes":
                inputs = data.getlist('inputs[]')
                outputs = data.getlist('outputs[]')
                scores = data.getlist('scores[]')
                description = data.getlist('description[]')
                count = data.get('count')
                question_id = data.get('question_id')
                question = Question.objects.get(pk = int(question_id))
                
                for i in range(int(count)):
                    tc = Testcase.objects.create(Tinput=inputs[i],Toutput=outputs[i])
                    tc.save()
                    q_tc = Question_Testcase.objects.create(testcase=tc, question = question, score = scores[i], description = description[i])
                    q_tc.save()
                    print(inputs[i], outputs[i], scores[i], description[i])
                res = {'msg':'Successflly saved testcases'} 
                messages.success(request, f'Question( Title : {question.Title},id : {question.id}) Added Successfully')
                return HttpResponse(json.dumps(res), content_type="application/json")
        else:
            return HttpResponse(json.dumps(form.errors), content_type="application/json")      
    else:
        form = QuestionCreateForm()
    return render(request, 'challenge/question_create_form.html',{'form':form,'model_name':'Question'})

























def completed_testpage(request):
    return render(request,'challenge/completed_test.html')
def test_instruction(request,pk,c_id):
    challenge = Challenge.objects.get(pk=pk)
    candidate = Candidate.objects.get(pk=c_id)
    count = challenge_questions.objects.filter(challenge = challenge ).count()
    return render(request,'challenge/test_instruction.html',{'challenge':challenge,'candidate':candidate,'question_count':count})

def candidate_form(request,challenge_id):
    test = Challenge.objects.get(pk=challenge_id)
    candidate = Candidate.objects.filter(user=request.user)
    print(candidate)
    if candidate.filter(test_name= test).first() is None:
        if request.method == "POST":
            form= CandidateDetailsForm(request.POST,request.FILES)
            if form.is_valid():
                form.instance.user = request.user
                form.instance.test_name = test
                form.save()
                return redirect('test_instruction',pk=challenge_id,c_id=form.instance.id)     
        else:
            form= CandidateDetailsForm()
        return render(request,'challenge/candidate_details.html',
                                {'form':form}
                                )
    else:
        c = candidate.filter(test_name = test).first()
        return redirect('test_instruction',pk=challenge_id,c_id=c.id)




def testpage(request,challenge_id,c_id):
    challenge = Challenge.objects.get(pk=challenge_id)
    candidate = Candidate.objects.get(pk=c_id)
    contest_questions = challenge_questions.objects.filter(challenge=challenge)
    candidate_codes_obj = Candidate_codes.objects.filter(candidate=candidate)
    question_ids = set()
    for t in contest_questions:
        if t.question!= None:
            question_ids.add(t.question.pk)
    questions = Question.objects.filter(pk__in = question_ids)
    print(questions)
    if candidate.completed_status is False:
       
        candidate_codes_obj = Candidate_codes.objects.filter(candidate=candidate)
        c= candidate.count
        candidate.count = c+1
        candidate.save()

        if candidate.count<=1:
            duration = challenge.Test_Duration
            candidate.start_time=datetime.now()
            candidate.end_time=datetime.now()+timedelta(minutes=duration+330)
            
            candidate.save()
            for q in contest_questions:
                questions.add(q.question)
                candidate_question_code = Candidate_codes(question=q.question,candidate=candidate)
                candidate_question_code.c_code = q.default_c_code
                candidate_question_code.cpp_code = q.default_cpp_code
                candidate_question_code.csharp_code = q.default_csharp_code
                candidate_question_code.java_code = q.default_java_code
                candidate_question_code.python_code = q.default_python_code
                candidate_question_code.save()
        
        if request.is_ajax() and request.method == "POST" :
            code_output=""
            if request.POST.get('code_draft')=='yes':
                q_id = request.POST.get('q_id')
                question = Question.objects.get(pk=q_id)
                language = request.POST.get('language')
                code = request.POST.get('code')
                candidate_question_code = candidate_codes_obj.filter(question=question).first()
                save_codes(candidate_question_code,code,language,question)
                res={'msg':'successfully saved'}
                return HttpResponse(json.dumps(res), content_type="application/json")
            if request.POST.get('submit_test')=='yes':
                candidate.completed_status = True
                candidate.save()
                total_score=0
                for i in candidate_codes_obj:
                    total_score+=i.score
                candidate.total_score = total_score
                candidate.save()
                print(candidate,candidate.total_score)
                print('submission request Total Score:',total_score)
                return redirect('submittedpage',challenge_id=challenge_id,c_id=c_id)
            if request.POST.get('question') == 'yes':
                
                q_id = request.POST.get('q_id')
                question = Question.objects.get(pk=q_id)
                candidate_question_code =""
                for i in candidate_codes_obj:
                    if i.question.id is question.id:
                        candidate_question_code = i
                return question_codes(candidate_question_code,question)
            if request.POST.get('full_screen') == 'yes':
                candidate.suspicious_count+=1
                candidate.save() 
            if request.POST.get('compile_run') == 'yes':
                code_output = save_run(request,candidate_codes_obj)
                res={'msg':code_output}
                return HttpResponse(json.dumps(res), content_type="application/json")
            
            if request.POST.get('submit_code')=='yes':
                print("code submission request")
                q_id = request.POST.get('q_id')
                question = Question.objects.get(pk=q_id)
                language = request.POST.get('language')
                code = request.POST.get('code')
                candidate_question_code = candidate_codes_obj.filter(question=question).first()
                save_codes(candidate_question_code,code,language,question)
                print(question)
                testcase = testcases.objects.filter(question=question).first()
                print(testcase)
                return validate_testcases(code,testcase,candidate_question_code,language,request,candidate)
        return render(request,'challenge/testpage.html',{'challenge':challenge,'questions':questions,'candidate':candidate,'candidate_codes':candidate_codes_obj,})
    else:
        return redirect('completed_testpage')

def submittedpage(request,challenge_id,c_id):
    return render(request,'challenge/test_submitted_successfully.html')
    
def save_run(request,candidate_codes_obj):
    q_id = request.POST.get('q_id')
    question = Question.objects.get(pk=q_id)
    language = request.POST.get('language')
    code = request.POST.get('code')
    custom_input = request.POST.get('input')
    candidate = candidate_codes_obj.first().candidate
    candidate_question_code = candidate_codes_obj.filter(question=question).first()
    save_codes(candidate_question_code,code,language,question)
    code_output = compile_run(language,code,custom_input,request,candidate)
    print("***compile_run",code_output)
    return code_output
  
def save_codes(candidate_question_code,code,language,question):
    print("saving question")
    if language == "Python":
        candidate_question_code.python_code=code
        candidate_question_code.save()
    elif language == "C":
        candidate_question_code.c_code=code
        candidate_question_code.save()
    elif language == "C++":
        candidate_question_code.cpp_code=code
        candidate_question_code.save()
    elif language == "Java":
        candidate_question_code.java_code=code
        candidate_question_code.save()
    elif language == "C#":
        candidate_question_code.csharp_code=code
        candidate_question_code.save()  

def question_codes(candidate_question_code,question):
    codes = {
        'python':candidate_question_code.python_code,
        'java':candidate_question_code.java_code,
        'csharp':candidate_question_code.csharp_code,
        'cpp':candidate_question_code.cpp_code,
        'c':candidate_question_code.c_code,
        'sample_input': question.sample_inputs,
    }
    # print(codes)
    return HttpResponse(json.dumps(codes), content_type="application/json")

def validate_testcases(code,testcase,candidate_question_code,language,request,candidate):
    candidate_question_code.submitted_code = code
    candidate_question_code.save()
    tc_input1 = testcase.input1.replace("\r\n","\n")
    tc_input2 = testcase.input2.replace("\r\n","\n")
    tc_input3 = testcase.input3.replace("\r\n","\n")
    tc_input4 = testcase.input4.replace("\r\n","\n")
    tc_input5 = testcase.input5.replace("\r\n","\n")
    output1 = compile_run(language,code,tc_input1,request,candidate)
    output2 = compile_run(language,code,tc_input2,request,candidate)
    output3 = compile_run(language,code,tc_input3,request,candidate)
    output4 = compile_run(language,code,tc_input4,request,candidate)
    output5 = compile_run(language,code,tc_input5,request,candidate)
    output1 =output1.replace("\n","")
    output2 =output2.replace("\n","")
    output3 =output3.replace("\n","")
    output4 =output4.replace("\n","")
    output5 =output5.replace("\n","")
    output1 =output1.strip()
    output2 =output2.strip()
    output3 =output3.strip()
    output4 =output4.strip()
    output5 =output5.strip()
    tc_output1 = testcase.output1
    tc_output1 = tc_output1.replace("\r\n","")
    tc_output2 = testcase.output2
    tc_output2 = tc_output2.replace("\r\n","")
    tc_output3 = testcase.output3
    tc_output3 = tc_output3.replace("\r\n","")
    tc_output4 = testcase.output4
    tc_output4 = tc_output4.replace("\r\n","")
    tc_output5 = testcase.output5
    tc_output5 = tc_output5.replace("\r\n","")
    passed_icon = "<img class='status-icon' src=\"/static/img/icon-yes.svg\" alt=\"Passed\">"
    failed_icon = "<img class='status-icon' src=\"/static/img/icon-no.svg\" alt=\"Failed\">"
    testcase_result={'tcdescription1':'your code failed for basic testcases','tcstatus1':'Failed '+failed_icon,'tcscore1':0,
                     'tcdescription2':'your code failed for medium testcases','tcstatus2':'Failed '+failed_icon,'tcscore2':0,
                     'tcdescription3':'your code failed for large testcases','tcstatus3':'Failed '+failed_icon,'tcscore3':0,
                     'tcdescription4':'your code failed for exceptional cases','tcstatus4':'Failed '+failed_icon,'tcscore4':0,
                     'tcdescription5':'your code failed hidden cases','tcstatus5':'Failed '+failed_icon,'tcscore5':0}
    output1 =output1.strip()
    print(tc_output1.encode('UTF-8'),"____",output1.encode('UTF-8'),tc_output1==output1)
    if(output1==tc_output1):
        testcase_result['tcdescription1']='your code passed for basic testcases'
        testcase_result['tcstatus1']='Passed '+passed_icon
        testcase_result['tcscore1']=10
    if(output2==tc_output2):
        testcase_result['tcdescription2']='your code passed for medium testcases'
        testcase_result['tcstatus2']='Passed '+passed_icon
        testcase_result['tcscore2']=10
    if(output3==tc_output3):
        testcase_result['tcdescription3']='your code passed for large testcases'
        testcase_result['tcstatus3']='Passed '+passed_icon
        testcase_result['tcscore3']=20
    if(output4==tc_output4):
        testcase_result['tcdescription4']='your code passed for exceptional cases'
        testcase_result['tcstatus4']='Passed '+passed_icon
        testcase_result['tcscore4']=20
    if(output5==tc_output5):
        testcase_result['tcdescription5']='your code passed for hidden cases'
        testcase_result['tcstatus5']='Passed '+passed_icon
        testcase_result['tcscore5']=40

    score = testcase_result['tcscore1']+testcase_result['tcscore2']+testcase_result['tcscore3']+testcase_result['tcscore4']+testcase_result['tcscore5']
    if candidate_question_code.score < score:
        candidate_question_code.score = score
        candidate_question_code.save()
    candidate_code_marks  =Candidate_codes.objects.filter(candidate = candidate)
    total_score = 0
    for i in candidate_code_marks:
        total_score+=i.score
    candidate.total_score = total_score
    candidate.save()
    
    return HttpResponse(json.dumps(testcase_result),content_type="application/json")
