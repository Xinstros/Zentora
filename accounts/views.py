from django.shortcuts import render, redirect
from .forms import SignupForm

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
    #if request.user.account_type != 'DEV':
        #return redirect('marketplace')  # Placeholder for marketplace
    return render(request, 'accounts/timeline.html', {})