from django.shortcuts import render

# Create your views here.
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
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
                return redirect("home")
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
            return redirect('home')

    context={'article_form':form,'data':data}
    return render(request,"home.html",context)

def article(request):

    data = RegisterForm.objects.all().last()

    form = ArticleForm()
    if request.method=='POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context={'article_form':form,'data':data}
    return render(request,"home.html",context)

def all_articles(request):

    data = Article.objects.all()

    context={'data':data}
    return render(request,'allarticles.html',context)


def model(request):
    if request.GET:
        text = request.GET['textarea']
        stopwords = list(STOP_WORDS)
        nlp = spacy.load('en_core_web_sm')
        doc = nlp(text)
        tokens = [tokens.text for tokens in doc]
        word_freq = {}
        for word in doc:
            if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
                if word.text not in word_freq.keys():
                    word_freq[word.text] = 1
                else:
                    word_freq[word.text] += 1
        max_freq = max(word_freq.values())
        for word in word_freq.keys():
            word_freq[word] = word_freq[word] / max_freq
        sent_tokens = [sent for sent in doc.sents]
        sent_scores = {}
        for sent in sent_tokens:
            for word in sent:
                if word.text in word_freq.keys():
                    if sent not in sent_scores.keys():
                        sent_scores[sent] = word_freq[word.text]

                    else:
                        sent_scores[sent] += word_freq[word.text]
        select_len = int(len(sent_tokens) * 0.3)
        summary = nlargest(select_len, sent_scores, key=sent_scores.get)
        final_summary = [word.text for word in summary]
        summary = ' '.join(final_summary)
        len_text = len(text.split(' '))
        len_sum = len(summary.split(' '))
        context = {'result': summary,'text':text,'len_text':len_text,'len_sum':len_sum}
        return render(request,'model.html',context)

    return render(request, 'model.html')