from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class QuizzesSample(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_questions(self):
        return self.question_set.all()

    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"
        ordering = ['id']
