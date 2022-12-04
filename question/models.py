from django.db import models
from quizes.models import QuizzesSample
from django.core.exceptions import ValidationError


class Question(models.Model):
    title = models.CharField(max_length=255, verbose_name='Вопрос')
    quiz = models.ForeignKey(QuizzesSample, on_delete=models.CASCADE, verbose_name='Набор тестов')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

    def __str__(self):
        return self.title

    def get_answers(self):
        return self.answer_set.all()

    # def full_clean(self, exclude=None, validate_unique=True, validate_constraints=True):
    #     super().full_clean()
    #     answers = Answer.objects.filter(question=self.pk)
    #     if True not in [answer.is_right for answer in answers]:
    #         raise ValidationError(answers)
        # if True not in [answer.is_right for answer in self.answer_set.all()]:
        #     raise ValidationError([answer for answer in self.answer_set.all()])

    # def clean_fields(self, exclude=True):
    #     if True not in [answer.is_right for answer in self.answer_set.all()]:
    #         raise ValidationError([answer for answer in self.answer_set.all()] )
        #'Должен быть как минимум один правильный ответ !',
        # if Question.answer_set.all():
        #     raise ValidationError('Все ответы не могут быть правильными')

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class Answer(models.Model):
    text = models.CharField(max_length=255, verbose_name='Ответ')
    is_right = models.BooleanField(default=False, verbose_name='Правильный')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

    def __str__(self):
        return f'Вопрос - {self.question.title}, ответ - {self.text}, правильный - {"да" if self.is_right else "нет"}'

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"