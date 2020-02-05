import datetime

from django.db import models
from django.utils import timezone

class ToDo(models.Model):
    todo_name = models.CharField(max_length=100)
    todo_description = models.TextField()
    due_date = models.DateTimeField('due date')

    def __str__(self):
        return self.todo_name

    def is_past_due(self):
        return self.due_date > timezone.now()
