from django.http import Http404
from django.shortcuts import render, redirect
from django.db import models
from MainApp.models import Snippet
from django.core.exceptions import ObjectDoesNotExist

def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    context = {'pagename': 'Добавление нового сниппета'}
    return render(request, 'pages/add_snippet.html', context)


def snippets_page(request):
    snipp = Snippet.objects.all()
    num_of_snipps = len(snipp)
    context = {"items": snipp, "quantity": num_of_snipps}
    return render(request, 'pages/view_snippets.html', context)

def view_curr_snippet(request, item_id):
    try:
        cur_snip = Snippet.objects.get(id=item_id)
    except ObjectDoesNotExist:
        return render(request, "errors.html", {"error": f"Item with id={item_id} not found."})
    else:
        context = {"items": cur_snip,}
        return render(request, 'pages/view_snippet.html', context)

