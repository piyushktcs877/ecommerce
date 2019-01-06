from django import forms


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


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        data = self.cleaned_data()
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Password must match")
        return data






