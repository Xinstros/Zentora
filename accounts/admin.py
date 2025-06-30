
# Register your models here.
from django.contrib import admin
from .models import ZentoraUser, Task, Request

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'status', 'deadline', 'created_at']
    list_filter = ['status', 'deadline']
    search_fields = ['title', 'description']

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'reward_type', 'reward_amount', 'deadline']
    list_filter = ['reward_type', 'deadline']
    search_fields = ['title', 'description']

admin.site.register(ZentoraUser)