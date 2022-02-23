from rest_framework import serializers
from .models import *


class CreateQuiz(serializers.Serializer):
    name = serializers.CharField(required = True)
    category = serializers.CharField(required = False)


class QuestionAnswerSerializer(serializers.Serializer):
    name = serializers.CharField(required = False)
    quest = serializers.CharField(required = True)
    ans = serializers.CharField(required = True)


class QuizIDserializer(serializers.ModelSerializer):
    class Meta:
        model = QuizModel
        fields = ["id"]


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoreModel
        fields = ["score", "quiz"]
