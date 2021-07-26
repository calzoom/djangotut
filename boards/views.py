from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, Http404
from .models import Board, Topic, Post

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


def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)

    if request.method == "POST":
        subject = request.POST["subject"]
        message = request.POST["message"]

        user = User.objects.first()  # TODO: get the currently logged in user

        topic = Topic.objects.create(subject=subject, board=board, starter=user)

        post = Post.objects.create(message=message, topic=topic, created_by=user)

        return redirect(
            "board_topics", pk=board.pk
        )  # TODO: redirect to the created topic page

    return render(request, "new_topic.html", {"board": board})
