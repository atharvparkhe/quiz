# Generated by Django 4.0.2 on 2022-02-22 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizmodel',
            name='no_of_questions',
        ),
    ]
