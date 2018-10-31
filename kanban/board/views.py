from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from .serializers import *
from .models import *
import django_filters

User = get_user_model()

class KanbanBoardViewSet(viewsets.ModelViewSet):

    serializer_class = KanbanBoardSerializer
    queryset = KanbanBoard.objects.all()
    filter_fields = ("owner",)

    '''def get_queryset(self):

        """
        returns objects that must have owner as current user.
        """

        queryset = super(KanbanBoardViewSet, self).get_queryset()
        return queryset.filter(owner=self.request.user)'''

class ColumnViewSet(viewsets.ModelViewSet):

    serializer_class = ColumnSerializer
    queryset = Column.objects.all()
    filter_fields = ("board",)

class CardViewSet(viewsets.ModelViewSet):

    serializer_class = CardSerializer
    queryset = Card.objects.all()
    filter_fields = ("column",)
