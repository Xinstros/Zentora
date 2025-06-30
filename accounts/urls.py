from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('timeline/', views.timeline, name='timeline'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/create/', views.task_create, name='task_create'),
    path('tasks/<int:pk>/update/', views.task_update, name='task_update'),
    path('tasks/<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('requests/', views.request_list, name='request_list'),
    path('requests/create/', views.request_create, name='request_create'),
    path('requests/<int:pk>/update/', views.request_update, name='request_update'),
    path('requests/<int:pk>/delete/', views.request_delete, name='request_delete'),
    path('marketplace/', views.marketplace, name='marketplace'),
    path('artwork/', views.artwork_list, name='artwork_list'),
    path('artwork/create/', views.artwork_create, name='artwork_create'),
    path('artwork/<int:pk>/update/', views.artwork_update, name='artwork_update'),
    path('artwork/<int:pk>/delete/', views.artwork_delete, name='artwork_delete'),
    path('settings/', views.settings, name='settings'),
]