from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404

from tasks.models import TaskModel, UserModel


def list_view(request):
    tasks = TaskModel.objects.all()
    data = {
        'tasks': list(tasks.values())
    }
    return JsonResponse(data)


def about_view(request):
    return HttpResponse('About page')


def detail_view(request, uuid):
    task = get_object_or_404(TaskModel, id=uuid)
    data = {
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'status': task.status,
        'created_at': task.created_at,
        'updated_at': task.updated_at,
        'reporter': {
            'id': task.reporter.id,
            'username': task.reporter.username,
            'email': task.reporter.email
        },
        'assignee': {
            'id': task.assignee.id,
            'username': task.assignee.username,
            'email': task.assignee.email
        }
    }
    return JsonResponse(data, safe=False)


def create_view(request):
    task = TaskModel(
        title="New created task",
        reporter=UserModel.objects.get(id=1),
        assignee=UserModel.objects.get(id=3)
    )
    task.save()

    return HttpResponse(f'Created task {task.id}')


def update_view(request, uuid):
    task = get_object_or_404(TaskModel, id=uuid)
    task.title = "New Title"
    task.description = "content after upgrade"
    task.save()
    return HttpResponse(f'Task {uuid} updated')


def delete_view(request, uuid):
    task = get_object_or_404(TaskModel, id=uuid)
    task.delete()
    return HttpResponse(f'Delete task {uuid}')
