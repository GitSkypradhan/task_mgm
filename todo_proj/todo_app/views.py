from django.shortcuts import render, redirect, HttpResponse
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from .models import Task
from accounts.models import User
from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404


# Create your views here.

# task list is index page here
@login_required
def task_list(request):
    query = request.GET.get('q')
    if query:
        task = Task.objects.filter(Q(title__icontains=query) | Q(created_date__icontains=query))

    else:
        # query : select task by user logged in and order by date descending
        task = Task.objects.filter(user=request.user).order_by('-created_date')
        # task = Task.objects.all()
        items_per_page = 5
        paginator = Paginator(task, items_per_page)
        page_num = request.GET.get('page')
        task = paginator.get_page(page_num)
        task_list = paginator.get_page(page_num)

    return render(request, 'task_list.html', {'tasks': task, 'task_list': task_list})


@login_required
def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)  # query select * from Task where id =1 # only one object
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)

    return render(request, 'edit_task.html', {'form': form, 'task': task})


@login_required
def create_task(request):
    if request.method == 'POST':  # agar submit pe click kiya
        form = TaskForm(request.POST)  # form object of class TaskForm create (request.POST as parameter)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # set the logged-in user as the task's user
            task.save()
            return redirect("task_list")
    else:  # method is get
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})


@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')


@login_required
def manager_dash(request):
    total_tasks = Task.objects.count()
    tasks_pending = Task.objects.filter(status='pending').count()
    tasks_done = Task.objects.filter(status='completed').count()
    task_obj = Task.objects.order_by('-created_date')[:10]  #
    users = User.objects.values('id', 'username', 'role').filter(role='employee')

    task = {'Total_tasks': total_tasks,
            'Pending_tasks': tasks_pending,
            'Completed_tasks': tasks_done,
            }
    return render(request, "manager_dash.html", {'task': task, 'task_obj': task_obj, 'users': users})


@login_required
def employee_list(request, userid):
    users = User.objects.values('id', 'username', 'role').filter(role='employee')
    query = request.GET.get('q')
    if query:
        task = Task.objects.filter(Q(title__icontains=query) | Q(created_date__icontains=query))

    else:
        # query : select task by user logged in and order by date descending
        task = Task.objects.filter(user=userid).order_by('-created_date')
        total_tasks = task.count()
        pending_tasks = Task.objects.filter(user=userid,status='pending').count()
        compeleted_tasks = Task.objects.filter(user=userid,status='completed').count()
        taskbox = {'Total_tasks':total_tasks,'Pending_tasks':pending_tasks,'Completed_tasks':compeleted_tasks}
        items_per_page = 5
        paginator = Paginator(task, items_per_page)
        page_num = request.GET.get('page')
        task = paginator.get_page(page_num)
        task_list = paginator.get_page(page_num) # task list


    return render(request, 'employee_list.html', {'users': users, 'tasks': task, 'task_list': task_list,'userid':userid,'taskbox':taskbox})
