from django.shortcuts import render
from django.http import HttpResponse

from .models import Board
# Create your views here.


def home(request):
    board = Board.objects.all()
    boards_name = list()

    for bd in board:
        boards_name.append(bd.name)

    return HttpResponse('<br>'.join(boards_name))


