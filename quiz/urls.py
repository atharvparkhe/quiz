from django.urls import path
from . import views
from .views import *


urlpatterns = [
	path('create-quiz/', views.createQuiz, name="create-quiz"),
	path('set-quiz/<quiz_id>/', views.setQuiz, name="set-quiz"),
	path('quiz/<quiz_id>/', views.shareQuiz, name="share-quiz"),
	path('answer-quiz/<quiz_id>/', views.answerQuiz, name="answer-quiz"),
	path('result/<quiz_id>/', views.result, name="quiz"),
]