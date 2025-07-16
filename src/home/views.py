import pathlib
from django.shortcuts import render
from django.http import HttpResponse
from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent


def home_view(request, *arg, **kwargs):
    return about_view(request, *arg, **kwargs)


def about_view(request, *arg, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = qs.filter(path=request.path)
    try:
        percent = (page_qs.count() * 100.0) / qs.count()
    except:
        percent = 0

    my_title = "My Page"
    my_context = {
        "page_title": my_title,
        "page_visit_count": page_qs.count(),
        'total_visit_count': qs.count(),
        'percent': percent
    }
    path = request.path
    PageVisit.objects.create(path=path)
    html_template = 'home.html'
    return render(request, html_template, my_context)
