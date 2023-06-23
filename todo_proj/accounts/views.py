from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
from .forms import CustomPasswordResetForm


# Create your views here.

# authentication part here
def login_user(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            if user.role == 'manager':
                return redirect('manager_dash')
            if user.role == 'employee':
                return redirect("/")
        else:
            messages.error(request,"Invalid username or password.")


    form = LoginForm()
    return render(request,'login_user.html',{'form':form})

@login_required
def logout_user(request):
    logout(request)
    return render(request,'logout_user.html')

@login_required
def register(request):

    from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponse("<html>Registered Successfully <br> <a href='/accounts/login'>Login</a> "
                                "<a href='/manager_dash'>Back</a></html>")  # Redirect to the desired URL after successful registration

    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


# pasword reset view


class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset.html'
    form_class = CustomPasswordResetForm
    success_url = reverse_lazy('password_reset_done')

