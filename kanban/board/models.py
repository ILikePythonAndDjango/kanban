from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Card(models.Model):

    title = models.CharField(max_length=200)
    content = models.TextField()
    column = models.ForeignKey('Column', on_delete=models.CASCADE   )

    def __str__(self):
        return self.title

class Column(models.Model):

    title = models.CharField(max_length=200)
    board = models.ForeignKey('KanbanBoard', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class KanbanBoard(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
