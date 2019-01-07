from django import forms
from django.contrib.auth import get_user_model

class ContactForm(forms.Form):
    fullname = forms.CharField(
                        widget=forms.TextInput(
                            attrs={
                                "id":"fullname",
                                "class":"form-control",
                                "placeholder":"you full name"
                            }))
    email = forms.EmailField(
                        widget=forms.EmailInput(
                            attrs={
                                "id": "Email",
                                "class": "form-control",
                                "placeholder": "Enter Email"
                            }))

    content = forms.CharField(
                        widget=forms.Textarea(
                            attrs={
                                "id": "content",
                                "class": "form-control",
                                "placeholder": "Enter content"
                            }))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email is not Valid")
        return email


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField( widget=forms.PasswordInput())


User = get_user_model()


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if "gmail.com" not in email:
            raise forms.ValidationError("email not correct")
        qs = User.objects.filter(username=email)
        if qs.exists():
            raise forms.ValidationError("username already exists")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Password must match")
        return data






