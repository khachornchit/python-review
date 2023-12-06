from django.shortcuts import render
from django.http import HttpResponse


def math_sum(x, y):
    return x + y


def say_hello(request):
    result = math_sum(5, 10)
    return render(request, 'index.html', {'math_sum': result})
