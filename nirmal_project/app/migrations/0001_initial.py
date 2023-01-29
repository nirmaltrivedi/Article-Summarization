# Generated by Django 4.1.3 on 2022-11-20 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('password1', models.CharField(max_length=150)),
                ('password2', models.CharField(max_length=150)),
                ('occupation', models.CharField(max_length=150)),
                ('organization', models.CharField(max_length=150)),
            ],
        ),
    ]
