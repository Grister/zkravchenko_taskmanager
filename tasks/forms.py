from django import forms
from django.contrib.auth import get_user_model

from tasks.models import TaskModel


class TaskCreateForm(forms.Form):
    title = forms.CharField(max_length=32, widget=forms.TextInput(attrs={
         'class': "form-control"}))
    description = forms.CharField(required=False, widget=forms.TextInput(attrs={
         'class': "form-control"}))

    assignee = forms.ModelChoiceField(queryset=get_user_model().objects.all(), widget=forms.Select(attrs={
        'class': "form-control"
    }))

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(TaskCreateForm, self).__init__(*args, **kwargs)

    def save(self):
        task = TaskModel(
            title=self.cleaned_data['title'],
            description=self.cleaned_data['description'],
            assignee=self.cleaned_data['assignee'],
            reporter=self.user,
        )
        task.save()
        return task


class TaskUpdateForm(forms.Form):
    title = forms.CharField(max_length=64, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))
    status = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    assignee = forms.ModelChoiceField(required=False, queryset=get_user_model().objects.all(), widget=forms.Select(attrs={
        'class': "form-control"
    }))
