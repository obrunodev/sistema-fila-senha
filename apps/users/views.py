from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from apps.users.forms import UserUpdateForm, UserRegisterForm
from apps.users.models import User


def user_signup(request):
    """
    A view to register a new user.
    """
    if request.method == 'GET':
        form = UserRegisterForm()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username'].lower()
            already_exists = User.objects.filter(
                username=username
            ).first()
            if already_exists:
                messages.error(request, 'User already exists.')
                return redirect('signup')
            new_user = form.save()
            new_user.set_password(form.cleaned_data['password'])
            return redirect('users:login')
    
    context = {'form': form}
    return render(request, 'users/register.html', context)


@login_required
def user_update(request):
    """
    A view to update self information.
    """
    user = request.user
    if request.method == 'GET':
        form = UserUpdateForm(instance=user)
    
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dados atualizados!')
            return redirect('users:update')
    
    context = {'form': form}
    return render(request, 'users/update.html', context)
