from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(RegisterForm)
admin.site.register(LoginForm)
admin.site.register(Article)