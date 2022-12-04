from django.db import models
from quizes.models import QuizzesSample
from users.models import CustomUser


class Score(models.Model):
    quiz = models.ForeignKey(QuizzesSample, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    right_answers = models.FloatField()

    def __str__(self):
        return self.pk
