from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import *
from .models import *

def login_view(request):
    form = SignIn(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            data = RegisterForm.objects.filter(email=email).values()
            pass1 = None
            for i in data:
                pass1 = i['password1']
            if password == pass1:
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"login_form": form, "msg": msg})


def register_user(request):
    msg = None

    if request.method == "POST":
        form = SignUp(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            msg = 'Form is not valid'
    else:
        form = SignUp()

    return render(request, "accounts/register.html", {"register_form": form, "msg": msg})

def home(request):

    data = RegisterForm.objects.all().last()

    form = ArticleForm()
    if request.method=='POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={'article_form':form,'data':data}
    return render(request,"home.html",context)

def article(request):

    data = RegisterForm.objects.all().last()

    form = ArticleForm()
    if request.method=='POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={'article_form':form,'data':data}
    return render(request,"home.html",context)

def all_articles(request):

    data = Article.objects.all()

    context={'data':data}
    return render(request,'allarticles.html',context)