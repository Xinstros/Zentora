from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('timeline/', views.timeline, name='timeline'),
]