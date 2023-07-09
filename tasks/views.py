from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DeleteView, CreateView, TemplateView, DetailView, UpdateView

from tasks.forms import TaskCreateForm, TaskUpdateForm
from tasks.models import TaskModel


class TaskListView(ListView):
    model = TaskModel
    template_name = 'tasks/index.html'
    ordering = ['-created_at']


class AboutPageView(TemplateView):
    template_name = 'about.html'


class TaskDetailView(DetailView):
    model = TaskModel
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'

    def get_object(self, queryset=None):
        uuid = self.kwargs.get('uuid')
        return get_object_or_404(TaskModel, id=uuid)


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = TaskModel
    form_class = TaskCreateForm
    template_name = 'tasks/task_create.html'
    success_url = '/tasks/'
    login_url = '/sign-in/'

    def form_valid(self, form):
        form.instance.reporter = self.request.user
        return super(TaskCreateView, self).form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = TaskModel
    form_class = TaskUpdateForm
    login_url = '/sign-in/'
    template_name = 'tasks/task_update.html'
    success_url = '/tasks'

    def get_object(self, queryset=None):
        uuid = self.kwargs.get('uuid')
        return get_object_or_404(TaskModel, id=uuid)

    def get(self, request, *args, **kwargs):
        task = self.get_object()
        if request.user not in (task.reporter, task.assignee):
            return redirect('tasks:index')

        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.assignee = form.cleaned_data['assignee'] or self.request.user
        return super().form_valid(form)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = TaskModel
    login_url = '/sign-in/'
    template_name = "tasks/confirm_delete.html"
    success_url = '/'

    def get_object(self, queryset=None):
        uuid = self.kwargs.get('uuid')
        return get_object_or_404(TaskModel, id=uuid)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.reporter != request.user or self.object.status:
            return redirect('tasks:index')

        return super().get(request, *args, **kwargs)
