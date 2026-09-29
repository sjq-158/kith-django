from django import forms
from django.contrib.auth.password_validation import validate_password

from .models import Branch, User


class RegisterForm(forms.ModelForm):
    branch = forms.ModelChoiceField(queryset=Branch.objects.filter(is_active=True))
    role = forms.ChoiceField(
        choices=[("pharmacist", "Pharmacist"), ("head_pharmacist", "Head Pharmacist")]
    )
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    field_order = ["email", "branch", "role", "password1", "password2"]

    class Meta:
        model = User
        fields = ["email", "branch", "role"]

    def clean(self):
        cleaned = super().clean()
        p1, p2 = cleaned.get("password1"), cleaned.get("password2")
        if p1 and p2:
            if p1 != p2:
                self.add_error("password2", "Passwords do not match.")
            else:
                try:
                    validate_password(p1)
                except forms.ValidationError as error:
                    self.add_error("password1", error)
        return cleaned

    def save(self, commit=True):
        user = super().save(commit=False)
        user.company = user.branch.company
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user