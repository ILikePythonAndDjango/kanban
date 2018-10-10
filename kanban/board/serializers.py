from rest_framework import serializers
from .models import *

class KanbanBoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = KanbanBoard
        fields = ('id', 'owner', 'title')

class ColumnSerializer(serializers.ModelSerializer):

    class Meta:
        model = Column
        fields = ('id', 'board', 'title')

class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = ('id', 'content', 'column', 'title')
