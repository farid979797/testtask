from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'task/index.html')

def categories(request, menuitem_id):
    context = {
        'cat_selected': menuitem_id
    }
    return render(request, 'task/category_page.html', context=context)
