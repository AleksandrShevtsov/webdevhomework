from django.contrib import admin
import myapp.models

# Register your models here.
admin.site.register(myapp.models.Task)
admin.site.register(myapp.models.Category)
admin.site.register(myapp.models.SubTask)


