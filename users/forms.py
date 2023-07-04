from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError

UserModel = get_user_model()


class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=32, widget=forms.TextInput(attrs={
         'class': "form-control", 'placeholder': "Enter your username"}))
    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={
         'class': "form-control", 'placeholder': "Enter your first name"}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={
         'class': "form-control", 'placeholder': "Enter your last name"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': "form-control", 'placeholder': "Enter your email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control", 'placeholder': "Enter your password"}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control", 'placeholder': "Confirm your password"}))

    def clean_username(self) -> str:
        username = self.cleaned_data["username"]
        try:
            UserModel.objects.get(username=username)
            raise ValidationError("Username is already registered")
        except UserModel.DoesNotExist:
            return username

    def clean_email(self) -> str:
        email = self.cleaned_data["email"]
        try:
            UserModel.objects.get(email=email)
            self.add_error("email", "Email is already registered")
        except UserModel.DoesNotExist:
            return email

    def clean(self) -> None:
        try:
            password = self.cleaned_data["password"]
            confirm_password = self.cleaned_data["confirm_password"]
            if password != confirm_password:
                self.add_error("confirm_password", "Passwords does not match")
        except KeyError:
            self.add_error("password", "Enter your password")

    def save(self):
        cleaned_data = self.cleaned_data
        del cleaned_data["confirm_password"]

        return UserModel.objects.create_user(**cleaned_data)


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=32, widget=forms.TextInput(attrs={
        'class': "form-control", 'placeholder': "Enter your username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control", 'placeholder': "Enter your password"}))

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user or not user.is_active:
                self.add_error('username', 'Invalid username or password')

        return cleaned_data
