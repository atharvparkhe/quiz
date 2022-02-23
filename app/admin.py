from django.contrib import admin
from .models import *

admin.site.register(UserModel)
admin.site.register(CategoryModel)


class AnswerModelAdmin(admin.StackedInline):
    model = AnswerModel

class QuestionModelAdmin(admin.ModelAdmin):
    inlines = [ AnswerModelAdmin ]

admin.site.register(QuestionModel, QuestionModelAdmin)