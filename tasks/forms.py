from django import forms
from django.contrib.auth import get_user_model

from tasks.models import TaskModel


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['title', 'description', 'assignee']

    title = forms.CharField(
        max_length=32,
        widget=forms.TextInput(attrs={
            'class': "form-control"
        })
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': "form-control"
        })
    )
    assignee = forms.ModelChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.Select(attrs={
            'class': "form-control"
        })
    )


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['title', 'description', 'status', 'assignee']

    title = forms.CharField(
        max_length=64,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    status = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    assignee = forms.ModelChoiceField(
        required=False,
        queryset=get_user_model().objects.all(),
        widget=forms.Select(attrs={'class': "form-control"})
    )
