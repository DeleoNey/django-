from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth import logout
# ProfileUpdateForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created! You are now able to log in.!")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def logout_view(request): # view for logout method allows to loging out making POST request
    if request.method == "POST":
        logout(request)
        return redirect('login')

    return render(request, 'users/logout.html')

@login_required(login_url='login')
def profile(request):
    return render(request, 'users/profile.html')