from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from base.models import *
from app.models import *


class QuizModel(BaseModel):
    creator = models.ForeignKey(UserModel, related_name="user_set_quiz", on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryModel, related_name="user_set_quiz_category", on_delete=models.CASCADE)
    def __str__(self):
        return self.creator.name


class QuizItemsModel(BaseModel):
    quiz = models.ForeignKey(QuizModel, related_name="set_quiz_items", on_delete=models.CASCADE)
    question = models.ForeignKey(QuestionModel, related_name="set_quiz_question", on_delete=models.CASCADE)
    correct_answer = models.ForeignKey(AnswerModel, related_name="set_quiz_answer", on_delete=models.CASCADE)


class AnswerQuizModel(BaseModel):
    player = models.ForeignKey(UserModel, related_name="user_answering_quiz", on_delete=models.CASCADE)
    quiz = models.ForeignKey(QuizModel, related_name="answering_quiz", on_delete=models.CASCADE)
    question = models.ForeignKey(QuestionModel, related_name="answered_quiz_question", on_delete=models.CASCADE)
    answer = models.ForeignKey(AnswerModel, related_name="answered_quiz_answer", on_delete=models.CASCADE)


class ScoreModel(BaseModel):
    user = models.ForeignKey(UserModel, related_name="user_score", on_delete=models.CASCADE)
    quiz = models.ForeignKey(QuizModel, related_name="quiz_score", on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

@receiver(post_save, sender=AnswerQuizModel)
def calculate_score(sender, instance, *args, **kwargs):
    try:
        quiz = instance.quiz
        user = instance.player
        score_obj = ScoreModel.objects.get(user=user, quiz=quiz)
        ans_quiz_objs = AnswerQuizModel.objects.filter(player=user, quiz=quiz)
        x=0
        for obj in ans_quiz_objs:
            if quiz.set_quiz_items.filter(question=obj.question, correct_answer=obj.answer).count() == 1:
                x += 1
        score_obj.score = x
        score_obj.save()
    except Exception as e:
        print(e)
    # print("###################")

