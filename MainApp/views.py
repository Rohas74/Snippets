from django.http import Http404
from django.shortcuts import render, redirect
from django.db import models
from MainApp.models import Snippet
from django.core.exceptions import ObjectDoesNotExist
from MainApp.forms import SnippetForm


def create_snippet(request):
   if request.method == "POST":
       form = SnippetForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect("view_snip")
       return render(request,'pages/add_snippet.html',{'form': form})

def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    if request.method =="GET":
        form = SnippetForm()
    #Snippet.objects.create(name='Функция ввода данныхы', lang="py", code='def my_input(): a = input(str) return a')
        context = {
            'pagename': 'Добавление нового сниппета',
            'form': form
            }
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
        return render(request, "pages/errors.html", context | {"error": f"Item with id={item_id} not found."})
    else:
        context = {"items": cur_snip,}
        return render(request, 'pages/view_snippet.html', context)

