from django.shortcuts import redirect


def index(request):
    user = request.user
    
    if not user.is_authenticated:
        return redirect('users:login')

    if user.is_superuser:
        return redirect('tasks:list')
    else:
        return redirect('tasks:list')