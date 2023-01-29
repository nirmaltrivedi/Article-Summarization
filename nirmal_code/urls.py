from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_view, name='login'),
    path('home/', home, name='home'),
    path('articles/', all_articles, name='articles'),
    path('', model, name="model"),
]