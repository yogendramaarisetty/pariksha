import os
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import UserRegisterForm,CandidateDetailsForm,QuestionCreateForm,ContestCreationForm, Test_Feedback_Form
from .models import demoCodes,Candidate,Challenge,Question,Candidate_codes,Testcase,challenge_questions,Question_Testcase, Test_Feedback
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
import os
from django.conf import settings
from django.http import HttpResponse, Http404

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
            # print(current_site)
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
    # print('\n\n\n\n',test_count,'\n\n\n')
    context ={
        'challenges':Challenge.objects.all(),
        'test_count': test_count
    }
    return render(request,'challenge/challenges.html',context)


@user_passes_test(lambda u: u.is_superuser)
def create_contest_form(request):
    if request.method == "POST":
        form = ContestCreationForm(request.POST)
        # print('form is post',request.POST)
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
                    # print(Active)
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
                # print('CURRENT_CONTEST_ID = ',contest_id) 
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
    # print('\n\n\n\n',test_count,'\n\n\n')
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
                        # print(Active)
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
                # print('CURRENT_CONTEST_ID = ',contest_id) 
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
                    # print('question form saved successfully')
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
                    # print(inputs[i], outputs[i], scores[i], description[i])
                res = {'msg':'Successflly saved testcases'} 
                messages.success(request, f'Question( Title : {question.Title},id : {question.id}) Added Successfully')
                return HttpResponse(json.dumps(res), content_type="application/json")
        else:
            return HttpResponse(json.dumps(form.errors), content_type="application/json")      
    else:
        form = QuestionCreateForm()
    return render(request, 'challenge/question_create_form.html',{'form':form,'model_name':'Question'})

@user_passes_test(lambda u: u.is_superuser)
def question_edit_form(request, question_id):
    question = Question.objects.all().get(pk = question_id)
    question_testcases = Question_Testcase.objects.filter(question = question)
    existing_tc_count = question_testcases.count()
    if request.method == "POST":
        data = request.POST
        form = QuestionCreateForm(request.POST,instance = question)
        if request.is_ajax():
            if request.POST.get('question')=='yes':
                if form.is_valid():
                    form.save()
                    question = form.save(commit=False)
                    res = {'saved':'yes',
                            'msg':'Question Updated successfully',
                            'question_id': question.pk
                            }
                    # print('question form saved successfully')
                    return HttpResponse(json.dumps(res), content_type="application/json")
                else:
                    return HttpResponse(json.dumps({'errors':'yes','form_errors':form.errors}), content_type="application/json")
            elif request.POST.get('question_testcase') == "yes":
                etcids = data.getlist('etc_id_list[]')
                inputs = data.getlist('inputs[]')
                outputs = data.getlist('outputs[]')
                scores = data.getlist('scores[]')
                description = data.getlist('description[]')
                count = data.get('count')
                question_id = data.get('question_id')
                print(len(etcids),etcids)
                for e in range(0,len(etcids)):
                    curr_etc = Question_Testcase.objects.get(pk = int(etcids[e]))
                    tio = curr_etc.testcase
                    tio.Tinput=inputs[e]
                    tio.Toutput=outputs[e]
                    tio.save()
                    curr_etc.testcase=tio
                    curr_etc.score = scores[e]
                    curr_etc.description = description[e]
                    curr_etc.save()


                for i in range(existing_tc_count,int(count)):
                    tc = Testcase.objects.create(Tinput=inputs[i],Toutput=outputs[i])
                    tc.save()
                    q_tc = Question_Testcase.objects.create(testcase=tc, question = question, score = scores[i], description = description[i])
                    q_tc.save()
                    # print(inputs[i], outputs[i], scores[i], description[i])
                #Existing_cases
                # for j in range(1,question_testcases.count()+1):

                res = {'msg':'Successflly saved testcases'} 
                messages.success(request, f'Question( Title : {question.Title},id : {question.id}) Updated Successfully')
                return HttpResponse(json.dumps(res), content_type="application/json")
        else:
            return HttpResponse(json.dumps(form.errors), content_type="application/json")      
    else:
        form = QuestionCreateForm(instance= question)
        print(question_testcases)
    return render(request, 'challenge/question_edit_form.html',{'form':form,'model_name':'Question','question_testcases':question_testcases,'existing_tc_count':question_testcases.count()})

@user_passes_test(lambda u: u.is_superuser)
def download_result(request, contest_id):
    contest = Challenge.objects.get(pk = contest_id)
    candidates = Candidate.objects.order_by('-total_score','suspicious_count')
    candidates = candidates.filter(test_name = contest)
    createResultFile(candidates,contest.Title)
    path="results"
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

def createResultFile(candidates,name):
    
    file_path = os.path.join(settings.STATIC_ROOT, "media")
    print(file_path)
    os.chdir(file_path)
    open(name+".csv", 'w').close()
    results = open(name+".csv",'a+')
    header = "Full name, Roll Number , college, Mobile, suspicious rate, Total score\n"
    
    results.write(header)
    candidate_rows=""
    for candidate in candidates:
        candidate_rows += f'{candidate.fullname},{candidate.rollnumber},{candidate.college},{candidate.mobile_number},{candidate.suspicious_count},{candidate.total_score}\n'
    results.write(candidate_rows)
    results.close()
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(BASE_DIR)
def contact(request):
    return render(request,'challenge/contact.html')



@user_passes_test(lambda u: u.is_superuser)
def results(request):
    contests = Challenge.objects.all()
    return render(request,'challenge/results.html',{'challenges': contests})


@user_passes_test(lambda u: u.is_superuser)
def contest_results(request,contest_id):
    contest = Challenge.objects.get(pk = contest_id)
    candidates = Candidate.objects.order_by('-total_score','suspicious_count')
    candidates = candidates.filter(test_name = contest)
    createResultFile(candidates,"results")
    return render(request, 'challenge/contest_Results.html',{'contest':contest,'candidates':candidates})









def demo_ide(request):
    try:
        demo_codes = demoCodes.objects.create(user = request.user)
        demo_codes.save()
    except:
        demo_codes = demoCodes.objects.filter(user = request.user).first()
    print(demo_codes)
    questions = Question.objects.filter(Level="Demo Question")
    question = questions.first()
    print(questions)
    if request.is_ajax() and request.method == "POST" :
            code_output=""
            if request.POST.get('msg')=='fetch_current_question_codes':
                return question_codes(demo_codes,question)

            if request.POST.get('code_draft')=='yes':
                language = request.POST.get('language')
                code = request.POST.get('code')
                save_codes(demo_codes,code,language,question)
                res={'msg':'successfully saved'}
                return HttpResponse(json.dumps(res), content_type="application/json")
            elif request.POST.get('compile_run') == 'yes':
                language = request.POST.get('language')
                custom_input = request.POST.get('input') 
                code = request.POST.get('code')
                print(repr(code))
                save_codes(demo_codes,code,language,question)
                code_output = compile_run(language,code,custom_input,request,request.user)
                return HttpResponse(json.dumps(code_output), content_type="application/json")
            elif request.POST.get('submit_code')=='yes':
                language = request.POST.get('language')
                code = request.POST.get('code')
                save_codes(demo_codes,code,language,question)
                testcases = Question_Testcase.objects.filter(question=question)
                return validate_testcases(code,testcases,demo_codes,language,request,request.user,'demo')
    return render(request,'challenge/demoIDE.html',{'questions':questions,'candidate_codes':demo_codes})









def completed_testpage(request,challenge_id,c_id):
    candidate = Candidate.objects.get(pk = c_id)
    if request.is_ajax() and request.method == "POST" :
        form= Test_Feedback_Form(request.POST)
        if form.is_valid():
            form.instance.Candidate = candidate
            try:
                form.save()
                res={'message': f'Thank you {candidate.fullname} ! We recieved your feedback.'}
            except:
                res={'message': f'Hey {candidate.fullname} ! We already recieved your feedback.'}
            
            return HttpResponse(json.dumps(res), content_type="application/json")     
    else:
        feedback = Test_Feedback.objects.filter(Candidate = candidate).first()
        if feedback == None: 
            form= Test_Feedback_Form()
            return render(request,'challenge/completed_test.html',
                                {'form':form}
                                )
        else:
            return render(request,'challenge/completed_test.html')
def test_instruction(request,pk,c_id):
    challenge = Challenge.objects.get(pk=pk)
    candidate = Candidate.objects.get(pk=c_id)
    count = challenge_questions.objects.filter(challenge = challenge ).count()
    return render(request,'challenge/test_instruction.html',{'challenge':challenge,'candidate':candidate,'question_count':count})

def candidate_form(request,challenge_id):
    test = Challenge.objects.get(pk=challenge_id)
    candidate = Candidate.objects.filter(user=request.user)
    # print(candidate)
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
        messages.success(request, f'Resume')
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
    for question in questions:
        create_candidate_codes(candidate,question)
    

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
        
        if request.is_ajax() and request.method == "POST" :
            code_output=""
            if request.POST.get('msg')=='fetch_current_question_codes':
                question = Question.objects.get(pk=int(request.POST.get('current_question_id')))
                current_question_codes = candidate_codes_obj.filter(question=question).first()
                return question_codes(current_question_codes,question)

            if request.POST.get('code_draft')=='yes':
                q_id = request.POST.get('q_id')
                question = Question.objects.get(pk=q_id)
                language = request.POST.get('language')
                code = request.POST.get('code')
                candidate_question_code = candidate_codes_obj.filter(question=question).first()
                save_codes(candidate_question_code,code,language,question)
                res={'msg':'successfully saved'}
                return HttpResponse(json.dumps(res), content_type="application/json")
            elif request.POST.get('submit_test')=='yes':
                candidate.completed_status = True
                candidate.save()
                total_score=0
                for i in candidate_codes_obj:
                    total_score+=i.score
                if candidate.total_score<total_score:
                    candidate.total_score = total_score
                candidate.save()
                # print(candidate,candidate.total_score)
                # print('submission request Total Score:',total_score)
                res={'msg':'successfully saved'}
                return HttpResponse(json.dumps(res), content_type="application/json")
            elif request.POST.get('question') == 'yes':
                
                q_id = request.POST.get('q_id')
                question = Question.objects.get(pk=q_id)
                candidate_question_code =""
                for i in candidate_codes_obj:
                    if i.question.id is question.id:
                        candidate_question_code = i
                return question_codes(candidate_question_code,question)
            elif request.POST.get('full_screen') == 'yes':
                candidate.suspicious_count+=1
                candidate.save() 
            elif request.POST.get('compile_run') == 'yes':
                code_output = save_run(request,candidate_codes_obj)
                return HttpResponse(json.dumps(code_output), content_type="application/json")
            elif request.POST.get('full_screen') == 'yes':
                candidate.suspicious_count+=1
                candidate.save() 
            elif request.POST.get('submit_code')=='yes':
                # print("code submission request")
                q_id = request.POST.get('q_id')
                question = Question.objects.get(pk=q_id)
                language = request.POST.get('language')
                code = request.POST.get('code')
                candidate_question_code = candidate_codes_obj.filter(question=question).first()
                save_codes(candidate_question_code,code,language,question)
                testcases = Question_Testcase.objects.filter(question=question)
                return validate_testcases(code,testcases,candidate_question_code,language,request,candidate,"")
        return render(request,'challenge/testpage.html',{'challenge':challenge,'questions':questions,'candidate':candidate,'candidate_codes':candidate_codes_obj,'end_time':candidate.end_time})
    else:
        return redirect('completed_testpage',challenge_id = challenge.id,c_id=candidate.id)

def submittedpage(request,challenge_id,c_id):
    return render(request,'challenge/test_submitted_successfully.html')

def create_candidate_codes(candidate,question):
    try:
        Candidate_codes.objects.create(candidate=candidate,question = question)
    except:
        pass
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
    # print("***compile_run",code_output)
    return code_output
  
def save_codes(candidate_question_code,code,language,question):
    # print("saving question")
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
    }
    # print(codes)
    return HttpResponse(json.dumps(codes), content_type="application/json")

def validate_testcases(code,testcases,candidate_question_code,language,request,candidate,flag):
    score = 0
    tc_status_list = {}
    index=0
    
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for tc in testcases:
        tc_input = tc.testcase.Tinput.replace("\r\n","\n")
        tc_output = tc.testcase.Toutput.replace("\r\n","")
        tc_output+="\n"
        output = compile_run(language,code,tc_input,request,candidate)
        if(output['status'] == "Compilation Errors"):
            return HttpResponse(json.dumps(output),content_type="application/json")
        # output = output['output']
        # os.chdir(BASE_DIR)
        # expout = open("expected"+str(index)+".txt",'w')
        # myout = open("myout"+str(index)+".txt",'w')
        # expout.write(tc_output)
        # myout.write(output)
        tcjson = {}
        if output['status'] == "Run Time Errors" :
            tcjson = {'description':tc.description,'score':0,'status' : "Run Time Errors", "error" : output['error'],'Time_taken':output['Timetaken']}
        elif output['status'] == "Timelimit exception":
            tcjson = {'description':tc.description,'score':0,'status' : "Timelimit exception", "error" : output['error'],'Time_taken': output['Timetaken']}
        elif output['status'] == "Successfully ran":
            if(tc_output == output['output']):
                score += tc.score
                tcjson = {'description':tc.description,'score':tc.score,'status':'Passed','Time_taken':output['Timetaken']}
            else:
                tcjson = {'description':tc.description,'score':0,'status':'Failed','Time_taken':output['Timetaken']}
        tc_status_list[index] = tcjson
        index+=1
    if flag!="demo":
        updateCandidateScores(candidate_question_code,candidate,score)
    
    
    return HttpResponse(json.dumps(tc_status_list),content_type="application/json")

def updateCandidateScores(candidate_question_code,candidate,score):
    if candidate_question_code.score < score:
        candidate_question_code.submitted_code = code
        candidate_question_code.score = score
        candidate_question_code.save()
    candidate_code_marks  =Candidate_codes.objects.filter(candidate = candidate)
    total_score = 0
    for i in candidate_code_marks:
        total_score+=i.score
    if candidate.total_score < total_score:
        candidate.total_score = total_score
    candidate.save()
