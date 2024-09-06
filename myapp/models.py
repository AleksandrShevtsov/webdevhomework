from django.contrib.auth.base_user import AbstractBaseUser
from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth.models import UserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        _("username"),
        max_length=50,
        unique=True,
        error_messages={
            "unique": _("A user with that username already exists."),
        }
    )
    first_name = models.CharField(
        _("first name"),
        max_length=40,
        validators=[MinLengthValidator(2)],
    )
    last_name = models.CharField(
        _("last name"),
        max_length=40,
        validators=[MinLengthValidator(2)],
    )
    email = models.EmailField(
        _("email address"),
        max_length=150,
        unique=True
    )
    phone = models.CharField(max_length=15, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(
        name="registered", auto_now_add=True
    )
    last_login = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "username",
        "first_name",
        "last_name",
    ]

    objects = UserManager()

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'task_manager_category'
        verbose_name = 'Category'
        unique_together = ('name',)


class Task(models.Model):
    STATUS_CHOICES = [
        ('New', 'New'),
        ('In progress', 'In progress'),
        ('Pending', 'Pending'),
        ('Blocked', 'Blocked'),
        ('Done', 'Done'),
    ]
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    sub_tasks = models.ManyToManyField('SubTask', related_name='tasks', null=True, blank=True)
    categories = models.ManyToManyField('Category', related_name='tasks', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'task_manager_task'
        ordering = ['-created_at']
        verbose_name = 'Task'
        unique_together = ('title',)


class SubTask(models.Model):
    STATUS_CHOICES = [
        ('New', 'New'),
        ('In progress', 'In progress'),
        ('Pending', 'Pending'),
        ('Blocked', 'Blocked'),
        ('Done', 'Done'),
    ]
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'task_manager_subtask'
        ordering = ['-created_at']
        verbose_name = 'SubTask'
        unique_together = ('title',)

