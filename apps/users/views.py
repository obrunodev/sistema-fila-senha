from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from apps.users.forms import UserUpdateForm


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
