
# Register your models here.
from django.contrib import admin
from .models import ZentoraUser, Task, Request, Artwork

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

@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'license', 'price', 'created_at']
    list_filter = ['license']
    search_fields = ['title']

admin.site.register(ZentoraUser)