
# Register your models here.
from django.contrib import admin
from .models import ZentoraUser, Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'status', 'deadline', 'created_at']
    list_filter = ['status', 'deadline']
    search_fields = ['title', 'description']

admin.site.register(ZentoraUser)