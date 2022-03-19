from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect


def index(request):
    return HttpResponse('Site about women')


def categories(request, catid):
    return HttpResponse(f"<h1>Categories</h1><p>{catid}</p>")


def archive(request, year):
    # if int(year) > 2022:
    #     raise Http404()
    if int(year) > 2022:
        return redirect('home', permanent=True)
    return HttpResponse(f"<h1>Archive of the documents</h1><p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not Found !</h1>')
