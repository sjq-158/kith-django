from django import forms
from django.contrib.auth.password_validation import validate_password
from django.db import transaction

from apps.profiles.models import HeadPharmacist, Pharmacist

from .models import Branch, User

ROLE_PROFILES = {
    "pharmacist": Pharmacist,
    "head_pharmacist": HeadPharmacist,
}


class RegisterForm(forms.ModelForm):
    # Stored in the role table (Pharmacist / HeadPharmacist), not in User
    first_name = forms.CharField(
        label="First Name", max_length=255,
        widget=forms.TextInput(attrs={"placeholder": "Jane"}),
    )
    last_name = forms.CharField(
        label="Last Name", max_length=255,
        widget=forms.TextInput(attrs={"placeholder": "Doe"}),
    )
    branch = forms.ModelChoiceField(
        label="Branch Location / ID",
        queryset=Branch.objects.filter(is_active=True),
        empty_label="e.g. Main Branch #1",
    )
    role = forms.ChoiceField(
        choices=[("pharmacist", "Pharmacist"), ("head_pharmacist", "Head Pharmacist")]
    )
    email = forms.EmailField(
        label="Professional Email", max_length=255,
        widget=forms.EmailInput(attrs={"placeholder": "pharmacist@kith.com"}),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"placeholder": "••••••••••••"}),
    )

    field_order = ["first_name", "last_name", "branch", "role", "email", "password"]

    class Meta:
        model = User
        fields = ["email", "branch", "role"]

    def clean_password(self):
        password = self.cleaned_data["password"]
        validate_password(password)
        return password

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.company = user.branch.company
        user.set_password(self.cleaned_data["password"])
        user.save()
        ROLE_PROFILES[user.role].objects.create(
            user=user,
            first_name=self.cleaned_data["first_name"],
            last_name=self.cleaned_data["last_name"],
        )
        return user

# edited - 09292026
# from django import forms
# from django.contrib.auth.password_validation import validate_password

# from .models import Branch, User


# class RegisterForm(forms.ModelForm):
#     branch = forms.ModelChoiceField(queryset=Branch.objects.filter(is_active=True))
#     role = forms.ChoiceField(
#         choices=[("pharmacist", "Pharmacist"), ("head_pharmacist", "Head Pharmacist")]
#     )
#     password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
#     password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

#     field_order = ["email", "branch", "role", "password1", "password2"]

#     class Meta:
#         model = User
#         fields = ["email", "branch", "role"]

#     def clean(self):
#         cleaned = super().clean()
#         p1, p2 = cleaned.get("password1"), cleaned.get("password2")
#         if p1 and p2:
#             if p1 != p2:
#                 self.add_error("password2", "Passwords do not match.")
#             else:
#                 try:
#                     validate_password(p1)
#                 except forms.ValidationError as error:
#                     self.add_error("password1", error)
#         return cleaned

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.company = user.branch.company
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user