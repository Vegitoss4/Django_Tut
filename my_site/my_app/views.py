from unittest import result
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound, Http404

# Create your views here.
articles = {
    'sports': 'Sports Page',
    'finance': 'Finance Page',
    'politics': 'Politics Page'
}

def index(request):
    return HttpResponse("Hello, world. You're at the my_app index.")

def simple_view(request):
    return HttpResponse("Simple View")

# def sports_view(request):
#     return HttpResponse(articles['sports'])

# def finance_view(request):
#     return HttpResponse(articles['finance'])

def news_view(request, topic):
    try:
        result = articles[topic]
        return HttpResponse(result)
    except:
        raise Http404("404 Generic Error") #404.html

def add_view(request, num1, num2):
    # domain.com/my_app/num1/num2/ --> num1 + num2
    add_result = num1 + num2
    result = f"{num1} + {num2} = {add_result}"
    return HttpResponse(str(result))