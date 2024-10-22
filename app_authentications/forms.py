from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label="Tên đăng nhập")
    password = forms.CharField(widget=forms.PasswordInput, label="Mật khẩu")

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Mật khẩu')
    password_confirm = forms.CharField(widget=forms.PasswordInput, label='Xác nhận mật khẩu')

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        labels = {
            'username': 'Tên đăng nhập',
            'email': 'Địa chỉ email',
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Mật khẩu không khớp!")
