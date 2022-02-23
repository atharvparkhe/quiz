from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from app.serializers import QAserializer
from .models import *


@api_view(["POST"])
def createQuiz(request):
    try:
        ser = CreateQuiz(data = request.data)
        if ser.is_valid():
            user, _ = UserModel.objects.get_or_create(name = ser.data["name"])
            user.save()
            cat = CategoryModel.objects.get(id = ser.data["category"])
            if not cat:
                return Response({"message":"Invalid Category ID"}, status=status.HTTP_406_NOT_ACCEPTABLE)
            quiz = QuizModel.objects.create(creator = user, category = cat)
            quiz_ser = QuizIDserializer(quiz)
            res_ser = QAserializer(cat.question_category.all(), many=True)
            payload = {
                "message":"Quiz Created. Add Quiz Items",
                "quiz" : quiz_ser.data,
                "questions":res_ser.data
            }
            return Response(payload, status=status.HTTP_201_CREATED)
        return Response({"error":ser.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error":str(e), "message":"Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
def setQuiz(request, quiz_id):
    try:
        quiz = QuizModel.objects.get(id=quiz_id)
        if not quiz:
            return Response({"message":"Invalid Quiz ID"}, status=status.HTTP_404_NOT_FOUND)
        ser = QuestionAnswerSerializer(data = request.data)
        if ser.is_valid():
            quest = QuestionModel.objects.get(id = ser.data["quest"])
            if not quest:
                return Response({"message":"Invalid Question ID"}, status=status.HTTP_406_NOT_ACCEPTABLE)
            ans = AnswerModel.objects.get(id = ser.data["ans"])
            if not ans:
                return Response({"message":"Invalid Answer ID"}, status=status.HTTP_406_NOT_ACCEPTABLE)
            QuizItemsModel.objects.get_or_create(quiz = quiz, question = quest, correct_answer = ans)
            return Response({"message":"Quiz Item Added"}, status=status.HTTP_202_ACCEPTED)
        return Response({"error":ser.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error":str(e), "message":"Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(["POST"])
def shareQuiz(request, quiz_id):
    try:
        quiz = QuizModel.objects.get(id=quiz_id)
        if not quiz:
            return Response({"message":"Invalid Quiz ID"}, status=status.HTTP_404_NOT_FOUND)
        ser = CreateQuiz(data = request.data)
        if ser.is_valid():
            user, _ = UserModel.objects.get_or_create(name = ser.data["name"])
            user.save()
            a, _ = ScoreModel.objects.get_or_create(user=user, quiz=quiz)
            a.save()
            quiz_ser = QuizIDserializer(quiz)
            res_ser = QAserializer(quiz.category.question_category.all(), many=True)
            payload = {
                "message":"User Saved. Answer the Quiz now",
                "quiz" : quiz_ser.data,
                "questions":res_ser.data
            }
            return Response(payload, status=status.HTTP_200_OK)
        return Response({"error":ser.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error":str(e), "message":"Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
def answerQuiz(request, quiz_id):
    try:
        quiz = QuizModel.objects.get(id=quiz_id)
        if not quiz:
            return Response({"message":"Invalid Quiz ID"}, status=status.HTTP_404_NOT_FOUND)
        ser = QuestionAnswerSerializer(data = request.data)
        if ser.is_valid():
            quest = QuestionModel.objects.get(id = ser.data["quest"])
            if not quest:
                return Response({"message":"Invalid Question ID"}, status=status.HTTP_406_NOT_ACCEPTABLE)
            ans = AnswerModel.objects.get(id = ser.data["ans"])
            if not ans:
                return Response({"message":"Invalid Answer ID"}, status=status.HTTP_406_NOT_ACCEPTABLE)
            user = UserModel.objects.get(name = ser.data["name"])
            if not user:
                return Response({"message":"Invalid User Name"}, status=status.HTTP_406_NOT_ACCEPTABLE)
            obj, _ = AnswerQuizModel.objects.get_or_create(player = user, quiz = quiz, question = quest, answer = ans)
            obj.save()
            return Response({"message":"Answer Saved"}, status=status.HTTP_202_ACCEPTED)
        return Response({"error":ser.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error":str(e), "message":"Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
def result(request, quiz_id):
    try:
        quiz = QuizModel.objects.get(id=quiz_id)
        if not quiz:
            return Response({"message":"Invalid Quiz ID"}, status=status.HTTP_404_NOT_FOUND)
        ser = CreateQuiz(data = request.data)
        if ser.is_valid():
            user = UserModel.objects.get(name = ser.data["name"])
            res_ser = ScoreSerializer(ScoreModel.objects.get(quiz=quiz, user=user))
            return Response({"data":res_ser.data}, status=status.HTTP_200_OK)
        return Response({"error":ser.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error":str(e), "message":"Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
