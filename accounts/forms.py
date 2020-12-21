from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from accounts.models import MyUser


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=60)

    class Meta:
        model = MyUser
        fields = ('email', 'username', 'password1', 'password2')


class AccountAuthenticationForm(forms.ModelForm):
    username = forms.CharField(label='username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('username', 'password')

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
