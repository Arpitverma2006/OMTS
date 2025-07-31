from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from OTS.models import *
import random
import datetime

def welcome(request):
    template=loader.get_template('welcome.html')
    return HttpResponse(template.render())

def candidateRegistrationForm(request):
    res=render(request,'registration_form.html')
    return res



def candidateRegistration(request):
    if request.method=='POST':
        username=request.POST['username']
        # check if the user already exists
        if len(Candidate.objects.filter(username=username)):
            userStatus=1
        else:
            candiate=Candidate()
            candiate.username=username
            candiate.password=request.POST['password']
            candiate.name=request.POST['name']
            candiate.save()
            userStatus=2
    else:
        userStatus=3 #Request method is not POST
    context = {
        'userStatus':userStatus
    }
    return(render(request,'registration.html',context))
    

def loginView(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        candidate=Candidate.objects.filter(username=username,password=password)
        if len(candidate)==0:
            loginError='Invalid Username or Password'
            res=render(request,'login.html',{'loginError':loginError})
        else:
            #login Success
            request.session['username']=candidate[0].username
            request.session['name']=candidate[0].name
            res=HttpResponseRedirect("home")
    else:
        res=render(request,'login.html')
    return res

def candidateHome(request):
    if 'name' not in request.session.keys():
        res=HttpResponseRedirect("login")
    else:
        res=render(request,'home.html')
    return res

def testPaper(request):
    if 'name' not in request.session.keys():
        res=HttpResponseRedirect("login")
    #fetch question from database table
    n=request.GET.get('n')
    question_pool=list(Question.objects.all())
    random.shuffle(question_pool)
    question_list=question_pool[:int(n)]
    context={'questions':question_list, 'test_duration': 30}  # 30 minutes
    return render(request, 'test_paper.html', context)



def calculateTestResult(request):
    # Ensure user is logged in
    if 'name' not in request.session.keys():
        return HttpResponseRedirect("login")

    total_attempt = 0
    total_right = 0
    total_wrong = 0
    qid_list = []

    # Extract question IDs from POST data
    for k in request.POST:
        if k.startswith('qno'):
            try:
                qid_list.append(int(request.POST[k]))
            except ValueError:
                continue

    # Calculate right and wrong answers
    for n in qid_list:
        try:
            question = Question.objects.get(qid=n)
            # Use .get() for safety and .upper() for case-insensitive comparison of answers
            # Assuming question.ans is stored in uppercase ('A', 'B', 'C', 'D')
            submitted_answer = request.POST.get('q' + str(n))
            if submitted_answer and question.ans == submitted_answer.upper():
                total_right += 1
            else:
                total_wrong += 1 # Mark as wrong if not submitted or incorrect
        except Question.DoesNotExist:
            pass
        except KeyError:
            # This catch is for questions that were displayed but not answered (no radio selected)
            # They will contribute to 'total_attempt' but not 'right' or 'wrong'.
            # Since we now handle `if submitted_answer`, this KeyError might be less likely
            # if `request.POST.get()` is used, but it's good to keep if specific scenarios exist.
            total_wrong += 1 # Consider unanswered questions as wrong
            pass


    # Calculate points
    points = (total_right * 10) - (total_wrong * 5) if qid_list else 0

    # --- CRITICAL FIX for "result_instance is not defined" ---
    result_instance = None # Initialize result_instance outside the try block
    try:
        # Try to get the latest result for the user
        result_instance = Result.objects.filter(username__username=request.session['username']).latest('date', 'time')
    except Result.DoesNotExist:
        # If no previous result exists, create a new one
        try:
            candidate_obj = Candidate.objects.get(username=request.session['username'])
            result_instance = Result()
            result_instance.username = candidate_obj
        except Candidate.DoesNotExist:
            return HttpResponseRedirect("login") # Redirect if candidate not found (serious issue)
    except Candidate.DoesNotExist: # Catch if Candidate.objects.get fails in the .latest() filter
        return HttpResponseRedirect("login")

    # --- Now result_instance is guaranteed to be defined ---

    result_instance.attempt = len(qid_list)
    result_instance.right = total_right
    result_instance.wrong = total_wrong
    result_instance.points = points
    result_instance.date = datetime.date.today()
    result_instance.time = datetime.datetime.now().time()
    result_instance.save()

    # Update candidate table
    try:
        candidate = Candidate.objects.get(username=request.session['username'])
        candidate.test_attempted = candidate.test_attempted + 1 if candidate.test_attempted is not None else 1
        candidate.points = points
        candidate.save()
    except Candidate.DoesNotExist:
        return HttpResponseRedirect("login")

    # Render the template directly, passing the result_instance
    context = {
        'result': result_instance
    }
    return render(request, 'show_result.html', context)

def testResultHistory(request):
    if 'name' not in request.session.keys():
        return HttpResponseRedirect("login")

    try:
        candidate = Candidate.objects.get(username=request.session['username'])
    except Candidate.DoesNotExist:
        return HttpResponseRedirect("login")

    # This query is correct assuming Result.username is a ForeignKey to Candidate
    results = Result.objects.filter(username=candidate).order_by('-date', '-time') # Added ordering for better history display

    context = {'candidate': candidate, 'results': results}
    # --- CRITICAL FIX: Ensure this matches your HTML file name ---
    return render(request, 'candidate_history.html', context)
    # If your file is indeed named 'candidate_history.html', then keep that.
    # But if it's 'result_history.html', change it here.


def showTestResult(request):
     if 'name' not in request.session.keys():
        return HttpResponseRedirect("login")
        
     #fetch latest result from Result Table
     result=Result.objects.filter(username_id=request.session['username']).latest('date')
     context={'result':result}
     return render(request,'show_result.html',context)

def logoutView(request):
    if 'name'  in request.session.keys():
        del request.session['username']
        del request.session['name']
    return HttpResponseRedirect("login")