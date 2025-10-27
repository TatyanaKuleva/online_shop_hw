from django.contrib.auth.forms import UserCreationForm
from django import forms
from catalog.forms import StyleFormMixin

from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegisterForm(StyleFormMixin, UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'phone', 'avatar', 'country')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Пользователь с таким email уже существует.")
        return email

class UserProfileEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email', 'phone', 'avatar', 'country']
