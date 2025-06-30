from django.shortcuts import render, redirect
from .forms import SignupForm, TaskForm, RequestForm
from .models import Task, Request

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

def timeline(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.user.account_type != 'DEV':
        return redirect('marketplace')  # Placeholder for marketplace
    return render(request, 'accounts/timeline.html', {})

def task_list(request):
    if not request.user.is_authenticated or request.user.account_type != 'DEV':
        return redirect('login')
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'accounts/task_list.html', {'tasks': tasks})

def task_create(request):
    if not request.user.is_authenticated or request.user.account_type != 'DEV':
        return redirect('login')
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'accounts/task_form.html', {'form': form})

def task_update(request, pk):
    if not request.user.is_authenticated or request.user.account_type != 'DEV':
        return redirect('login')
    task = Task.objects.get(pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'accounts/task_form.html', {'form': form})

def task_delete(request, pk):
    if not request.user.is_authenticated or request.user.account_type != 'DEV':
        return redirect('login')
    task = Task.objects.get(pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'accounts/task_delete.html', {'task': task})

def request_create(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            request_obj = form.save(commit=False)
            request_obj.user = request.user
            request_obj.save()
            return redirect('request_list')
    else:
        form = RequestForm()
    return render(request, 'accounts/request_form.html', {'form': form})

def request_list(request):
    if not request.user.is_authenticated:
        return redirect('login')
    requests = Request.objects.filter(user=request.user)
    return render(request, 'accounts/request_list.html', {'requests': requests})