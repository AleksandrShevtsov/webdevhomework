import os
import django
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from myapp.models import Task, SubTask, Category

# Создаем категории
category_dev = Category.objects.create(name='Development')
category_design = Category.objects.create(name='Design')
category_devops = Category.objects.create(name='DevOps')

# Создаем задачи
task1 = Task.objects.create(
    title='Implement user authentication',
    description='Add user authentication to the application using Django\'s built-in authentication system.',
    status='New',
    deadline=datetime(2024, 7, 15, 17, 0, 0)
)
task1.categories.set([category_dev])

task2 = Task.objects.create(
    title='Design landing page',
    description='Create a visually appealing landing page for the application.',
    status='In progress',
    deadline=datetime(2024, 7, 20, 18, 0, 0)
)
task2.categories.set([category_design])

task3 = Task.objects.create(
    title='Setup CI/CD pipeline',
    description='Configure a continuous integration and deployment pipeline using GitHub Actions.',
    status='Pending',
    deadline=datetime(2024, 7, 25, 19, 0, 0)
)
task3.categories.set([category_devops])

# Создаем подзадачи
SubTask.objects.create(
    title='Create login view',
    description='Implement the view for user login.',
    task=task1,
    status='New',
    deadline=datetime(2024, 7, 10, 15, 0, 0)
)

SubTask.objects.create(
    title='Design wireframe',
    description='Create a wireframe for the landing page design.',
    task=task2,
    status='In progress',
    deadline=datetime(2024, 7, 12, 16, 0, 0)
)

SubTask.objects.create(
    title='Write deployment script',
    description='Write a script to automate the deployment process.',
    task=task3,
    status='New',
    deadline=datetime(2024, 7, 15, 17, 0, 0)
)

print("Данные успешно добавлены!")
