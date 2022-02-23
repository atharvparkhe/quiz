from rest_framework import serializers
from .models import *
import random


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        exclude = ["created_at", "updated_at"]

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerModel
        exclude = ["created_at", "updated_at", "question"]

class QAserializer(serializers.ModelSerializer):
    options = serializers.SerializerMethodField()
    class Meta:
        model = QuestionModel
        exclude = ["created_at", "updated_at"]
    def get_options(self, obj):
        payload = []
        try:
            ser = AnswerSerializer(obj.answers_question.all(), many=True)
            payload = ser.data
            return payload
        except Exception as e:
            print(e)