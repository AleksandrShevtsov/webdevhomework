from datetime import datetime, timedelta
from django.utils import timezone
import os
import django

# без этого ошибка:     from myapp.models import Task, SubTask
# ModuleNotFoundError: No module named 'myapp'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from myapp.models import Task, SubTask


# Создаем задачу Task
task = Task.objects.create(
    title="Prepare presentation",
    description="Prepare materials and slides for the presentation",
    status="New",
    deadline=timezone.now() + timedelta(days=3)
)

# Создаем подзадачи для "Prepare presentation"
subtask1 = SubTask.objects.create(
    title="Gather information",
    description="Find necessary information for the presentation",
    task=task,
    status="New",
    deadline=timezone.now() + timedelta(days=2)
)

subtask2 = SubTask.objects.create(
    title="Create slides",
    description="Create presentation slides",
    task=task,
    status="New",
    deadline=timezone.now() + timedelta(days=1)
)
print(f"Создана задача: {task.title}, срок выполнения: {task.deadline}")
print(f"Созданы подзадачa: {subtask1.title}, c сроком выполнения: {subtask1.deadline}")
print(f"Созданы подзадачa: {subtask2.title}, c сроком выполнения: {subtask2.deadline}")
print(30 * '-')

print("Вывести все задачи со статусом 'New'")
new_tasks = Task.objects.filter(status="New")
for task in new_tasks:
    print(task.title, task.description, task.deadline)
print(30 * '-')

print('Вывести все подзадачи, у которых статус "Done", но срок выполнения истек')
expired_subtasks_done = SubTask.objects.filter(status="Done", deadline__lt=timezone.now())
count = 0
for subtask in expired_subtasks_done:
    count += 1
    print(subtask.title, subtask.description, subtask.deadline)
print("Количество подзадач с истекшим сроком выполнения:", count)
print(30 * '-')

# Изменить статус "Prepare presentation" на "In progress"
task = Task.objects.get(title="Prepare presentation")
task.status = "In progress"
task.save()
print("изменен статус Prepare presentation на", task.status)
print(30 * '-')

# Изменить срок выполнения для "Gather information" на два дня назад
subtask1 = SubTask.objects.get(title="Gather information")
print(subtask1.deadline)
subtask1.deadline = subtask1.deadline - timedelta(days=2)
subtask1.save()
print("изменен срок выполнения для Gather information на", subtask1.deadline)
print(30 * '-')

# Изменить описание для "Create slides" на "Create and format presentation slides"
subtask2 = SubTask.objects.get(title="Create slides")
subtask2.description = "Create and format presentation slides"
subtask2.save()
print("изменен описание для Create slides на", subtask2.description)
print(30 * '-')

# Удалить задачу "Prepare presentation" и все ее подзадачи
task_to_delete = Task.objects.get(title="Prepare presentation")
task_to_delete.delete()
print("удалена задача Prepare presentation и все ее подзадачи")
