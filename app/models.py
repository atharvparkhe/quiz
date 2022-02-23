from django.db import models
from base.models import BaseModel
import random


class CategoryModel(BaseModel):
    category = models.CharField(max_length=50)
    img = models.ImageField(upload_to="cat", height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return self.category


class QuestionModel(BaseModel):
    category = models.ForeignKey(CategoryModel, related_name="question_category", on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    def __str__(self):
        return self.question


class AnswerModel(BaseModel):
    question = models.ForeignKey(QuestionModel, related_name="answers_question", on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)
    img = models.ImageField(upload_to="ans", height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return self.answer


class UserModel(BaseModel):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name