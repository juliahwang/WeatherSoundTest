from django.contrib.auth import models as auth_models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .MyUserManager import MyUserManager

__all__ = (
    'User',
)


# 사용자 정보 모델
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        _('email address'),
        max_length=255,
        unique=True,
        null=True,
    )
    username = models.CharField(_('username'), max_length=40, null=True, unique=True)
    first_name = models.CharField(_('first name'), max_length=20, default='')
    last_name = models.CharField(_('last name'), max_length=20, default='')

    # TODO img_profile - CustomImageField 설정 필요
    img_profile = models.ImageField(upload_to='member', blank=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    is_superuser = models.BooleanField(default=False)
    # name = models.CharField(max_length=100, default="")

    objects = MyUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    def __str__(self):
        return "username: {}".format(self.username if self.username else self.email)

    @property
    def is_staff(self):
        """일반 사용자인지 아니면 스태프 권한이 있는지?"""
        return self.is_admin

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])

    def has_module_perms(self, app_label):
        """user가 주어진 app_label에 해당하는 권한이 있는지, has_perm과 비슷"""
        if self.is_active and self.is_superuser:
            return True
        return auth_models._user_has_module_perms(self, app_label)

    def has_perm(self, perm, obj=None):
        if self.is_active and self.is_superuser:
            return True

        return auth_models._user_has_perm(self, perm, obj)

    def get_full_name(self):
        return self.email if self.email else self.username

    def get_short_name(self):
        return self.email if self.email else self.username
