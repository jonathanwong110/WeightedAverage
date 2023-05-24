from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

TASK_CHOICES = (
    ('task', 'TASK'),
    ('quiz', 'QUIZ'),
    ('exam', 'EXAM'),
)


class Assignment(models.Model):
    name = models.CharField(max_length=255)
    task = models.CharField(max_length=4, choices=TASK_CHOICES, default="task")
    grade = models.IntegerField()
    weight = models.IntegerField()

    def __str__(self):
        return self.name + ' | ' + self.task + ' | ' + str(self.grade) + ' | ' + str(self.weight)

    def get_absolute_url(self):
        # return reverse('assignment-detail', args=(str(self.id)))
        return reverse('home')