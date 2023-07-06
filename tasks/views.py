from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect

from tasks.forms import TaskCreateForm, TaskUpdateForm
from tasks.models import TaskModel, UserModel


def list_view(request):
    tasks = TaskModel.objects.all().order_by('-created_at')
    data = {
        'tasks': list(tasks)
    }
    return render(request, "tasks/index.html", data)


def about_view(request):
    return render(request, "about.html")


def detail_view(request, uuid):
    task = get_object_or_404(TaskModel, id=uuid)
    context = {'task': task}
    return render(request, "tasks/task_detail.html", context)


@login_required
def create_view(request):
    if request.method == 'POST':
        form = TaskCreateForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('tasks:index')
    else:
        form = TaskCreateForm(user=request.user)

    return render(request, 'tasks/task_create.html', {'form': form})


@login_required
def update_view(request, uuid):
    task = get_object_or_404(TaskModel, id=uuid)
    if request.user not in (task.reporter, task.assignee):
        return redirect('tasks:index')

    if request.method == 'POST':
        form = TaskUpdateForm(request.POST)
        if form.is_valid():
            task.title = form.cleaned_data['title']
            task.description = form.cleaned_data['description']
            task.status = form.cleaned_data['status']
            task.assignee = form.cleaned_data['assignee'] or task.assignee
            task.save()
            return redirect('tasks:index')
    else:
        form = TaskUpdateForm(initial={
            'title': task.title,
            'description': task.description,
            'status': task.status,
            'assignee': task.assignee
        })

    return render(request, 'tasks/task_update.html', {'form': form, 'task': task})


@login_required
def delete_view(request, uuid):
    task = get_object_or_404(TaskModel, id=uuid)
    if request.user == task.reporter and task.status is False:
        task.delete()
    return redirect('tasks:index')
