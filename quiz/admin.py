from django.contrib import admin
from .models import *

class AnswerQuizModelAdmin(admin.ModelAdmin):
    list_display = ["player", "quiz", "question", "answer"]

admin.site.register(AnswerQuizModel, AnswerQuizModelAdmin)

admin.site.register(QuizModel)

class QuizItemsModelAdmin(admin.ModelAdmin):
    list_display = ["quiz", "question", "correct_answer"]

admin.site.register(QuizItemsModel, QuizItemsModelAdmin)

class ScoreModelAdmin(admin.ModelAdmin):
    list_display = ["user", "quiz", "score"]

admin.site.register(ScoreModel, ScoreModelAdmin)