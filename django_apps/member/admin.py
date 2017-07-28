from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from .forms import UserChangeForm, UserCreationForm

User = get_user_model()


class MyUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
        (None, {'fields': ('email', 'username', 'img_profile', 'password')}),
        (_('Personal info'), {'fields': ('email',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_admin', 'is_superuser')}),
    )

    # User 생성시 필요한 필드셋 정의
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'img_profile', 'password1', 'password2'),
        }),
    )

    list_display = ('username', 'email', 'img_profile', 'is_admin')
    list_filter = ('is_admin',)
    search_fields = ('username', 'email')
    ordering = ("email", 'username')
    filter_horizontal = ('user_permissions',)


admin.site.register(User, MyUserAdmin)
