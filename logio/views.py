from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_user, logout as logout_user
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from .models import Content

# Create your views here.

def logio_index(request):
    return render(request, 'homepage.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password=password)
        if user is not None:
            login_user(request, user)
            return redirect('logio_index')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')


def register(request):
    if request.method == 'POST':
        # print("method post")
        firstname = request.POST['first_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request, 'Username already exists')
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.info(request, 'Email already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username = username, first_name = firstname, password = password1, email = email)
                user.save()
                print('user saved')
                return redirect('login')
        else:
            messages.info(request, 'Passwords not matching')
            return redirect('register')


    else:
        return render(request, 'register.html')


def logout(request):
    logout_user(request)
    return redirect('logio_index')


def submit_article(request):#works when user makes a new article(POST) or user opens article page(GET)
    
    if request.method == 'POST':
        a_title = request.POST['article_title']
        a_content = request.POST['article_content']
        a_body = request.POST['article_body']
        # a_image = request.POST['article_image'] #results in MultiValueDictKeyError at /submit_article/
        a_image = request.FILES['article_image']
        a_author = request.user
        print('user = ' + str(a_author))
        print('content added title '+str(a_title)+' by : '+str(a_author))
        new_article = Content()
        new_article.article_title = str(a_title)
        new_article.article_content = str(a_content)
        new_article.article_author = str(a_author)
        new_article.article_body = str(a_body)
        new_article.article_image = a_image
        new_article.save()
        return redirect('logio_index')
    
    else:
        return render(request, 'submit_article.html')


def user_all_article(request):
    my_name = str(request.user)
    my_work = []
    for i in Content.objects.all():
        if i.article_author == my_name:
            my_work.append(i)
    print(my_work)
    return render(request, 'user_all_article.html', {'my_work':my_work})


def user_specific_article(request, article_id):
    article = Content.objects.filter(id = article_id)
    return render(request, 'user_specific_article.html', {'article':article})


def all_article(request):
    all_art = Content.objects.all()
    print(all_art)
    # print(all_art[0].article_image)
    return render(request, 'all_art.html', {'all_art':all_art})