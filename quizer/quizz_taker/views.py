from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from quizz_giver.models import Results,QuesModel,Quizes




from django.http import HttpResponse

def quizes(request,id):

    if request.method == 'POST':
        cus=Results.objects.filter(name=request.POST['name'])
        questions=QuesModel.objects.filter(id=id)
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
           
            if q.ans ==  request.POST.get(q.question):
               
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        res=cus(
            get_score=score,
            percent = percent
        )
        res.save()
        return render(request,'Results.html',context,{'user':cus})
    else:
        questions=QuesModel.objects.all()
        return render(request,'quiz.html',{'name':cus,"questions":questions})

def quiz_page(request,id):
    questions=Quizes.objects.filter(id=id)
    if request.method=='POST':
        usname=request.POST['name']
        code = request.POST['code']
        if code==id:
            res=Results(
                name=usname
            )
            res.save()
            return redirect('/quizes/id')
        else:
            return HttpResponse("invalid quiz code")
    
    
    
