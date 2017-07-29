from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm

User = get_user_model()


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'email',
            'img_profile',
            'username',
            'password1',
            'password2',
            'is_active',
            'is_admin',
        )

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """
    User 업데이트 폼
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = (
            'email',
            'img_profile',
            'password',
            'username',
            'is_active',
            'is_admin',
        )

    def clean_password(self):
        return self.initial["password"]
