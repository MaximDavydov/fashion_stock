from django.shortcuts import render
from django.http import HttpResponse


def test_view(request):
    print(request.GET)
    return HttpResponse("Hello, Paul!")

def test_view_int(request, test_int):
    return HttpResponse(f"<h1>Hello, {request.GET['name']}</h1><em>{test_int}</em>")

def another_test_view(request, **kwargs):
    return HttpResponse(f'Im testing view, Im get {kwargs["sample"]} and some string: {kwargs["test_str"]}')