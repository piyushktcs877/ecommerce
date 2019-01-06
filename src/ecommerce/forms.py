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












