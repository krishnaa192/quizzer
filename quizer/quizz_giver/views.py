
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from .forms import *
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
# from quizz_giver.forms import NameForm
 
# Create your views here.


def home(request):

    return render(request,'index.html')


def addQuestion(request): 
    # link=Quizes.object.get(pk=pk) 
    Name_quiz= Quizes.objects.all()  
    if request.user.is_authenticated:
        form=addQuestionform()
        if(request.method=='POST'):
            form=addQuestionform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form,'Name_quiz':Name_quiz}
        return render(request,'quiz.html',context)
    else: 
        return redirect('home') 
 
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home') 
    else: 
        form = createuserform()
        if request.method=='POST':
            form = createuserform(request.POST)
            if form.is_valid() :
                user=form.save()
                return redirect('login')
        context={
            'form':form,
        }
        return render(request,'register.html',context)
 
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "username does not exist")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.error(request,"User not found")
       context={}
       return render(request,'logini.html',context)
 
def logoutPage(request):
    logout(request)
    return redirect('/')

def addquiz(request):
    if request.user.is_authenticated:
        form=QuizeForm()
        if(request.method=='POST'):
            form=QuizeForm(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('addQuestion')
        context={'form':form}
        return render(request,'addquiz.html',context)
    else: 
        return redirect('home') 

def profile(request):
    quiz=Quizes.objects.all()
    profile=request.user.profile
    
    return render(request,'profile.html',{'quiz':quiz,'profile':profile})

def about(request):
    return render(request,'About.html')