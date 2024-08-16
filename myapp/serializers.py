from rest_framework import serializers
from .models import Task, SubTask, Category


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'deadline']


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = ['created_at']


class SubTaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = ['id', 'title', 'description', 'status', 'deadline']
        read_only_fields = ['created_at']


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
