from django.db import models


class List(models.Model):
    list_id = models.CharField(max_length=255, unique=True)
    list_name = models.CharField(max_length=255)
    is_default = models.BooleanField(default=False)
    is_display = models.BooleanField(default=True)

    def __str__(self):
        return self.list_name


class Task(models.Model):
    list = models.ForeignKey(List, related_name='tasks', on_delete=models.CASCADE)
    task_id = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    priority = models.CharField(max_length=50)
    deadline = models.DateTimeField()
    comment = models.TextField()
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title
