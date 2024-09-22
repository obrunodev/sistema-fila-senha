from apps.departments.models import Department, Queue
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages


@login_required
def department_call(request):

    if request.method == 'GET':
        current_queue = Queue.objects.filter(user=request.user).last()
        context = {
            'section': 'call',
            'current_queue': current_queue,
        }
        return render(request, 'departments/call.html', context)

    if request.method == 'POST':
        user = request.user
        
        if '_next_queue' in request.POST:
            department = user.table.department
            next_queue = Queue.objects.filter(
                department=department,
                user__isnull=True,
            ).first()
            if next_queue:
                next_queue.user = user
                next_queue.save()
                messages.success(request, f'Chamando senha {next_queue}!')
            else:
                messages.warning(request, 'Não tem nenhuma senha aguardando no momento.')
        
        if '_call_again' in request.POST:
            current_queue = Queue.objects.filter(user=request.user).last()
            messages.success(request, f'Chamando senha {current_queue} novamente.')
        
        return redirect('departments:call')
            


@login_required
def manage_queue(request):

    if request.method == 'GET':
        departments = Department.objects.all()
        context = {
            'section': 'manage',
            'departments': departments,
        }
        return render(request, 'departments/manage.html', context)

    if request.method == 'POST':
        department = Department.objects.filter(id=request.POST.get('d_id')).first()
        queue_number = Queue.objects.filter(department=department).count() + 1
        if department:
            new_queue = Queue.objects.create(
                department=department,
                queue_number=queue_number,
            )
            messages.success(request, f'Gerado senha {new_queue} para {new_queue.department}.')
        return redirect('departments:manage')
