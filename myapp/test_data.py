import os
import django
import random
from datetime import datetime, timedelta

# Настройка среды Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from myapp.models import Category, Task, SubTask

Category.objects.all().delete()
Task.objects.all().delete()
SubTask.objects.all().delete()

# Фиксированные данные для примеров
CATEGORY_NAMES = ['Work', 'Home', 'Fitness', 'Hobby', 'Education']
TASK_TITLES = [
    'Complete project report', 'Clean the house', 'Go to the gym', 'Read a book',
    'Cook dinner', 'Fix the garden', 'Study Django', 'Plan the trip',
    'Learn German', 'Attend yoga class', 'Buy groceries', 'Write blog post',
    'Organize photos', 'Call mom', 'Update resume', 'Review PRs',
    'Plan birthday party', 'Research investments', 'Build a new website', 'Take out the trash'
]
STATUSES = ['New', 'In progress', 'Pending', 'Blocked', 'Done']
TASK_TO_SUBTASKS = {
    'Complete project report': ['Gather all data', 'Analyze results', 'Write introduction', 'Create graphs', 'Proofread report'],
    'Clean the house': ['Vacuum the living room', 'Clean the kitchen', 'Dust the furniture', 'Mop the floors', 'Take out the trash'],
    'Go to the gym': ['Warm up for 10 minutes', 'Do 3 sets of squats', 'Bench press 3 sets', 'Run on treadmill for 20 minutes', 'Cool down and stretch'],
    'Read a book': ['Read chapter 1', 'Read chapter 2', 'Summarize main points', 'Reflect on key themes', 'Finish the book'],
    'Cook dinner': ['Prepare ingredients', 'Chop vegetables', 'Cook the main course', 'Make a salad', 'Set the table'],
    'Fix the garden': ['Weed the garden beds', 'Prune the bushes', 'Water the plants', 'Plant new flowers', 'Clean up the tools'],
    'Study Django': ['Review Django models', 'Build a basic form', 'Create views for tasks', 'Implement pagination', 'Test the application'],
    'Plan the trip': ['Book flights', 'Reserve hotel', 'Research local attractions', 'Create a packing list', 'Confirm reservations'],
    'Learn German': ['Study vocabulary', 'Practice pronunciation', 'Watch a video lesson', 'Write a short essay in German', 'Speak with a language partner'],
    'Attend yoga class': ['Prepare yoga mat', 'Warm up', 'Follow instructor\'s lead', 'Practice breathing techniques', 'Cool down with meditation'],
    'Buy groceries': ['Make a list of needed items', 'Go to the grocery store', 'Pick fresh produce', 'Buy dairy products', 'Check out at the counter'],
    'Write blog post': ['Choose a topic', 'Research information', 'Write first draft', 'Edit and proofread', 'Publish the post'],
    'Organize photos': ['Sort photos by date', 'Delete duplicates', 'Create new albums', 'Edit selected photos', 'Backup the collection'],
    'Call mom': ['Find a convenient time', 'Plan topics to discuss', 'Check in on health and well-being', 'Share recent updates', 'Set a date for the next call'],
    'Update resume': ['Review current resume', 'Add recent work experience', 'Update skills section', 'Proofread document', 'Export to PDF format'],
    'Review PRs': ['Read through code changes', 'Test new features locally', 'Provide feedback in comments', 'Approve PR if everything is fine', 'Merge the PR into main branch'],
    'Plan birthday party': ['Choose a theme', 'Invite friends', 'Order cake and snacks', 'Decorate the venue', 'Set up music playlist'],
    'Research investments': ['Identify potential stocks or funds', 'Read financial reports', 'Compare historical performance', 'Consult with a financial advisor', 'Make investment decision'],
    'Build a new website': ['Choose a domain name', 'Set up hosting', 'Design the homepage', 'Develop the main functionality', 'Test and deploy the website'],
    'Take out the trash': ['Collect all garbage bags', 'Tie up the bags', 'Take bags to the trash bin outside', 'Check if recycling is sorted', 'Return bins to the house']
}
# Функция для создания случайной даты
def random_date():
    start_date = datetime.now()
    end_date = start_date + timedelta(days=random.randint(1, 30))
    return end_date

# Создаем 5 категорий
categories = []
for category_name in CATEGORY_NAMES:
    category, created = Category.objects.get_or_create(name=category_name)
    categories.append(category)

# Создаем 20 задач
tasks = []
for i, task_title in enumerate(TASK_TITLES):
    task = Task.objects.create(
        title=task_title,
        description=f"Description for {task_title}",
        status=random.choice(STATUSES),
        deadline=random_date(),
    )
    # Добавляем случайные категории к задаче
    task.categories.add(random.choice(categories))
    tasks.append(task)

    # Создаем от 1 до 5 подзадач для каждой задачи
    subtasks = TASK_TO_SUBTASKS.get(task_title, [])
    for subtasks_title in subtasks:
        SubTask.objects.create(
            title=subtasks_title,
            description=f"Description for {subtasks_title}",
            task=task,
            status=random.choice(STATUSES),
            deadline=task.deadline,
        )

print("Test data successfully created.")
