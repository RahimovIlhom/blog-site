from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserRegisterForm
from users.models import CustomUser


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


def login_view(request):
    print(request.user)
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'registration/login.html')
        else:
            return render(request, 'registration/login.html')


class RegisterView(CreateView):
    model = CustomUser
    form_class = UserRegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
