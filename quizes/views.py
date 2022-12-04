from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from .models import Category, QuizzesSample


class CategoryListView(ListView):
    model = Category
    template_name = 'home.html'


def quizes_view(request, category_pk):
    quizes = QuizzesSample.objects.filter(category=category_pk)

    return render(request, 'quiz/quiz_samples.html', context={'quizes': quizes})

@csrf_exempt
def quiz_view(request, category_pk, quiz_id):
    quiz = QuizzesSample.objects.get(pk=quiz_id)
    questions = []
    for question in quiz.get_questions():
        answers = []
        for answer in question.get_answers():
            answers.append(answer.text)
        questions.append({"question": question.title, "answers": answers})
    # questions = [{'question': question.title, 'answers': question.get_answers()} for question in quiz.get_questions().values()]

    result = request.body
    return render(request, 'quiz/quiz.html', context={'quiz': quiz, 'questions': questions, 'result': result})
    # return JsonResponse({
    #     'data': list(questions)
    # })

