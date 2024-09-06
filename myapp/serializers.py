from django.utils import timezone
from rest_framework import serializers
from .models import Task, SubTask, Category, User
from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
import re


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone',
            'last_login',
        )

class RegisterUserSerializer(serializers.ModelSerializer):
    re_password = serializers.CharField(
        max_length=128,
        write_only=True,
    )

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            're_password',
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        username = data.get('username')
        first_name = data.get('first_name')
        last_name = data.get('last_name')

        if not re.match('^[a-zA-Z0-9_]*$', username):
            raise serializers.ValidationError(
                "The username must be alphanumeric characters or have only _ symbol"
            )

        if not re.match('^[a-zA-Z]*$', first_name):
            raise serializers.ValidationError(
                "The first name must contain only alphabet symbols"
            )

        if not re.match('^[a-zA-Z]*$', last_name):
            raise serializers.ValidationError(
                "The last name must contain only alphabet symbols"
            )

        password = data.get("password")
        re_password = data.get("re_password")

        if password != re_password:
            raise serializers.ValidationError({"password": "Passwords don't match"})

        try:
            validate_password(password)
        except ValidationError as err:
            raise serializers.ValidationError({"password": err.messages})

        return data

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop('re_password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user



class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = ['id', 'title', 'description', 'status', 'deadline', 'created_at']


class TaskSerializer(serializers.ModelSerializer):
    subtasks = SubTaskSerializer(many=True, read_only=True)
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'deadline', 'subtasks', 'created_at']


class TaskDetailSerializer(serializers.ModelSerializer):
    subtasks = SubTaskSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'deadline', 'subtasks']


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = ['created_at']

    def validate_deadline(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Нельзя задать дедлайн в прошлом.")
        return value


class SubTaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = ['id', 'title', 'description', 'status', 'deadline']
        read_only_fields = ['created_at']


class CategorySerializer(serializers.ModelSerializer):
    tasks_count = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ['id', 'name', 'tasks_count']

    def get_tasks_count(self, obj):
        return obj.tasks.count()

class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

    def validate_name(self, value):
        if Category.objects.filter(name=value).exists():
            raise serializers.ValidationError("Категория с таким названием уже существует.")
        return value

    def create(self, validated_data):
        self.validate_name(validated_data.get('name'))
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'name' in validated_data and instance.name != validated_data['name']:
            self.validate_name(validated_data.get('name'))
        return super().update(instance, validated_data)
