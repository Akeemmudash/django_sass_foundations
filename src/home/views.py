import pathlib
from django.shortcuts import render
from django.http import HttpResponse

this_dir = pathlib.Path(__file__).resolve().parent


def home_page_view(request, *arg, **kwargs):
    my_title = "My Page"
    my_context = {
        "page_title": my_title
    }
    html_template = 'home.html'
    return render(request, html_template, my_context)
