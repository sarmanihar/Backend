from django.shortcuts import render
from .models import Room,Post
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.http import HttpResponse, JsonResponse

def home(request):
    return render(request, 'home.html')  

def teacher(request):
    if request.method == 'POST':
        if request.POST.get('Question') and request.POST.get('Answer1') and request.POST.get('Answer2') and request.POST.get('Answer3') and request.POST.get('Answer4') and request.POST.get('S_Answer'):
            post=Room()
            post.Question= request.POST.get('Question')
            post.Answer1= request.POST.get('Answer1')
            post.Answer2= request.POST.get('Answer2')
            post.Answer3= request.POST.get('Answer3')
            post.Answer4= request.POST.get('Answer4')
            post.S_Answer= request.POST.get('S_Answer')
            post.save()
                
            return render(request, 'teacher.html')  

    else:
        return render(request,'teacher.html')
def student(request):
    queryset=Room.objects.all()
    context={
    'object_list':queryset
    }
    if request.method == 'POST':
        if request.POST.get('ans') :
            post=Post()
            post.ans= request.POST.get('ans')
            post.save()
                
            return render(request, 'student.html',context)  

    else:
        return render(request,'student.html',context)
        
def marks(request):
    queryset1=Post.objects.all()
    queryset2=Room.objects.all()
    i1=queryset1.count()
    i2=queryset2.count()
    i3=5
    i4=12
    mark=0
    marks=0

    i1=i3+i1-1+4
    i2=i4+i2-1     
    queryset3=0
    queryset4=0
    while i3<=i1 and i4<=i2:
        
        queryset3=Post.objects.get(id=i3)
        queryset4=Room.objects.get(id=i4)
        print(queryset3.ans)
        print(queryset4.S_Answer)
        marks=marks+1   
        if(queryset3.ans == queryset4.S_Answer):
            mark=mark+1
        if(i3 == 7):
           i3=11
        i3=i3+1
        i4=i4+1    
    context={
    'object_list1':queryset1,
    'object_list2':queryset2,
    'counter1':queryset3,
    'counter2':queryset4,
    'mark':mark,
    'marks':marks
    }
    return render(request,'marks.html',context)
