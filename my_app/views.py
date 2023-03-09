from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Index")


def detail(request, question_id):
    return HttpResponse(f"Вы находитесь на странице вопроса №{question_id}")


def result(request, question_id):
    return HttpResponse(f"Результаты вопроса №{question_id}")


def vote(request, question_id):
    return HttpResponse(f"Вы проголосовали за №{question_id}")
