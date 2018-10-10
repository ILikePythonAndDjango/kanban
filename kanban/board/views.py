from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from .serializers import *
from .models import *

User = get_user_model()

class KanbanBoardViewSet(viewsets.ModelViewSet):

    serializer_class = KanbanBoardSerializer
    queryset = KanbanBoard.objects.all()

class ColumnViewSet(viewsets.ModelViewSet):

    serializer_class = ColumnSerializer
    queryset = Column.objects.all()

class CardViewSet(viewsets.ModelViewSet):

    serializer_class = CardSerializer
    queryset = Card.objects.all()
