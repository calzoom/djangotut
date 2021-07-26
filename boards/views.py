from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Board

# Create your views here.
# Views are Python functions that receive
# HttpRequest objects and return HttpResponse objects

# Receive a request as a parameter and return a response as a result
def home(request):
    boards = Board.objects.all()
    return render(request, "home.html", {"boards": boards})


def board_topics(request, pk):
    # obj.pk gets the primary key for a model
    try:
        board = Board.objects.get(pk=pk)
    except:
        raise Http404
    return render(request, "topics.html", {"board": board})
