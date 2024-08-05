import os
import django
from django.utils import timezone
import datetime

# Настройка Django окружения
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
# Убедитесь, что указано правильное имя вашего проекта
django.setup()

# Импорт моделей
from myapp.models import Category, Task, SubTask


def populate():
    # Создание категорий
    category1 = Category.objects.create(name="Work")
    category2 = Category.objects.create(name="Personal")
    category3 = Category.objects.create(name="Hobby")

    print(f"Created categories: {category1}, {category2}, {category3}")

    # Создание задач
    task1 = Task.objects.create(
        title="Finish Django project",
        description="Complete the Django project for the client",
        status="In progress",
        deadline=timezone.now() + datetime.timedelta(days=5),
        created_at=timezone.now()
    )

    task2 = Task.objects.create(
        title="Buy groceries",
        description="Buy milk, bread, and eggs",
        status="New",
        deadline=timezone.now() + datetime.timedelta(days=1),
        created_at=timezone.now()
    )

    task3 = Task.objects.create(
        title="Paint the living room",
        description="Paint the walls with the new color",
        status="Pending",
        deadline=timezone.now() + datetime.timedelta(days=7),
        created_at=timezone.now()
    )

    # Привязка категорий к задачам
    task1.categories.add(category1)
    task2.categories.add(category2)
    task3.categories.add(category3)

    print(f"Created tasks: {task1}, {task2}, {task3}")

    # Создание подзадач
    subtask1 = SubTask.objects.create(
        title="Set up project structure",
        description="Set up the initial project structure for the Django project",
        task=task1,
        status="Done",
        deadline=timezone.now() + datetime.timedelta(days=2),
        created_at=timezone.now()
    )

    subtask2 = SubTask.objects.create(
        title="Write views",
        description="Write the views for the project",
        task=task1,
        status="In progress",
        deadline=timezone.now() + datetime.timedelta(days=4),
        created_at=timezone.now()
    )

    subtask3 = SubTask.objects.create(
        title="Go to the supermarket",
        description="Visit the nearest supermarket to buy groceries",
        task=task2,
        status="New",
        deadline=timezone.now() + datetime.timedelta(hours=6),
        created_at=timezone.now()
    )

    subtask4 = SubTask.objects.create(
        title="Choose paint color",
        description="Choose the new color for the living room walls",
        task=task3,
        status="Pending",
        deadline=timezone.now() + datetime.timedelta(days=3),
        created_at=timezone.now()
    )

    print(f"Created subtasks: {subtask1}, {subtask2}, {subtask3}, {subtask4}")


if __name__ == "__main__":
    populate()
