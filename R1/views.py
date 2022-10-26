from tkinter import N
from django.shortcuts import render
from django.http import HttpResponse
from .models import signup, table, orders
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import auth
# Create your views here.
# username1=''
# usename=username1+User_name

username1 = ''


def signup1(request):
    if request.method == 'POST':
        if request.POST.get('User_name') and request.POST.get('First_name') and request.POST.get('Last_name') and request.POST.get('Email_id') and request.POST.get('Password') and request.POST.get('city') and request.POST.get('country') and request.POST.get('state') and request.POST.get('profession'):
            post = signup()

            post.User_name = request.POST.get('User_name')

            global username1
            username1 = username1 + request.POST.get('User_name')

            post.First_name = request.POST.get('First_name')
            post.Last_name = request.POST.get('Last_name')
            post.Email_id = request.POST.get('Email_id')
            post.Password = request.POST.get('Password')
            post.city = request.POST.get('city')
            post.country = request.POST.get('country')
            post.state = request.POST.get('state')
            post.profession = request.POST.get('profession')
            post.save()
            print(username1)
            # print(request.POST.get('First_name'))
            #success='your account has been created...'
            # return HttpResponse(success)
            return render(request, 'home2.html')
    else:
        return render(request, 'b.html')


def login(request):
    if request.method == 'POST':
        if request.POST.get('User_name1') and request.POST.get('Password1'):
            global username1
            username1 = username1 + request.POST.get('User_name1')
            password = request.POST.get('Password1')
            if signup.objects.filter(User_name=request.POST.get('User_name1')).exists() and signup.objects.filter(Password=password).exists():
                return render(request, 'home2.html')

            else:
                return render(request, 'testlogin.html')
    else:
        return render(request, 'c.html')


#username1 = 2


# def home2(request):
#    return render(request, 'test.html')


# just for checking....
def home2(request):
    print(username1)
    fgh = 0
    if username1 == '':
        context = {
            'abcd': 1,

        }
        print(type('abcd'))
        return render(request, 'home2.html', context)
    else:
        if signup.objects.filter(profession='Seller').exists():
            fgh = 1
        context = {
            'abcd': username1,
            'efgh': fgh,
        }
        return render(request, 'home2.html', context)


def showseller2(request):
    ab = username1
    # queryset=table.objects.all()
    quesryset = table.objects.filter(user=ab)

    # check it..not filter its get

    context = {
        'object_list3': quesryset,
    }
    if request.method == 'POST':
        if request.POST.get('amount') and request.POST.get('price') and request.POST.get('off') and request.POST.get('objectn'):
            post = table()
            post.objects.filter(obj=request.POST.get('objectn')).update(
                amount=request.POST.get('amount'))
            post.objects.filter(obj=request.POST.get('objectn')).update(
                price=request.POST.get('price'))
            post.objects.filter(obj=request.POST.get('objectn')).update(
                off=request.POST.get('off'))
            #post.obj = request.POST.get('amount')
            #post.price = request.POST.get('price')
            #post.off = request.POST.get('off')
            # post.save()
            quesryset = table.objects.filter(user=ab)
            context = {
                'object_list3': quesryset,
            }
            return render(request, 'f.html', context)
    else:
        return render(request, 'f.html', context)


#username1 = 234


def showseller1(request):
    print(username1)
    context = {

        'object_list1': username1,
        # 'object_list2': table.objects.get(user=username1),
        'object_list2': table.objects.filter(user=username1),
        'object_list3': signup.objects.get(User_name=username1),
        # 'object_list2': table.objects.all(),
        # 'object_list2': table.objects.filter(user=username1),
        # 'object_list3': signup.objects.filter(user=username1)
        # 'object_list3': signup.objects.all()
    }
    if request.method == 'POST':
        if request.POST.get('obj') and request.POST.get('user') and request.POST.get('country1') and request.POST.get('state1') and request.POST.get('city1'):
            post = table()

            post.obj = request.POST.get('obj')
            post.user = request.POST.get('user')
            post.city = request.POST.get('country1')
            post.state = request.POST.get('state1')
            post.country = request.POST.get('city1')

            post.save()
            return render(request, 'e.html', context)
    else:
        return render(request, 'e.html', context)


obj1 = None

# context=None

n = 0
context123 = None


def showbuyer1(request):
    if request.method == 'POST':
        global n
        n = n+1
        #quesryset = signup.objects.filter(User_name=username1).first()
        # queryset70 = table.objects.filter(
        # obj=obj1, city=quesryset.city, state=quesryset.state, country=quesryset.country)

        """context = {
            'object_list3': queryset70,
            'order': obj1,
            'buyer': username1,
        }"""
        if n == 1:
            if request.POST.get('obj4'):
                #MyTable.objects.filter(pk=some_value).update(field1='some value')
                obj1 = request.POST.get('obj4')
                quesryset = signup.objects.filter(User_name=username1).first()

                # print(quesryset)
                # print(quesryset.city)
                # print(quesryset.state)
                # print(quesryset.country)
                #buyercity = quesryset.city
                #buyerstate = quesryset.state
                #buyercountry = quesryset.country

                queryset70 = table.objects.filter(
                    obj=obj1, city=quesryset.city, state=quesryset.state, country=quesryset.country)
                # and table.objects.filter(
                # city=buyercity) and signup.objects.filter(state=buyerstate) and signup.objects.filter(country=buyercountry)

                # print(queryset70)
                global context123
                context123 = {
                    'object_list3': queryset70,
                    'order': obj1,
                    'buyer': username1,
                }
                #a = Register.objects.filter(email=emailx1).first()
                #request.session['session_name'] = a.email
                return render(request, 'g.html', context123)
                # return showbuyer2(request,context)
        elif n == 2:
            if request.POST.get('ord') and request.POST.get('sell') and request.POST.get('p'):
                post = orders()
                post.buye = request.POST.get('sell')
                post.order = request.POST.get('ord')
                post.p = request.POST.get('p')
                post.idd=post.objects.count()+1
                post.save()
                return render(request, 'g.html', context123)
    else:
        #quesryset = signup.objects.filter(User_name=234).first()
        # print(quesryset)
        # print(quesryset.city)
        # print(quesryset.state)
        # print(quesryset.country)
        
        return render(request, 'g.html')


def showseller3(request):
    if request.method == 'POST':
        if request.POST.get('d') and request.POST.get('d1'):
            post = orders()
            #post.objects.filter(id=8).update(dorn=request.POST.get('amount'))
            event = orders.objects.get(idd=request.POST.get('d1'))
            event.delete()
            quer = orders.objects.all()
            context = {
                'objeclist70': quer,
            }
            return render(request, 'h.html', context)
    else:
        quer = orders.objects.all()
        print(quer)
        context = {
            'objeclist70': quer,
        }
        
        return render(request, 'h.html',context)
