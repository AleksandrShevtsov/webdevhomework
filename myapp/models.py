from django.db import models


# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ('New', 'New'),
        ('In progress', 'In progress'),
        ('Pending', 'Pending'),
        ('Blocked', 'Blocked'),
        ('Done', 'Done'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    categories = models.ManyToManyField('Category', related_name='tasks')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class SubTask(models.Model):
    STATUS_CHOICES = [
        ('New', 'New'),
        ('In progress', 'In progress'),
        ('Pending', 'Pending'),
        ('Blocked', 'Blocked'),
        ('Done', 'Done'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=Task.STATUS_CHOICES)
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
