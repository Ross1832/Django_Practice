from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render
from .models import Women, Category


menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
        ]


def index(request):
    posts = Women.objects.all()
    cats = Category.objects.all()
    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'MAIN PAGE',
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=context)


def about(request):
    return render(request, 'women/about.html', {'title': 'ABOUT'})


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


def addpage(request):
    return HttpResponse('Add Page')


def contact(request):
    return HttpResponse('Contact')


def login(request):
    return HttpResponse('Login')


def show_post(request, post_id):
    return HttpResponse(f"Display the Article = {post_id}")


def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'MAIN PAGE',
        'cat_selected': cat_id,
    }
    return render(request, 'women/index.html', context=context)
