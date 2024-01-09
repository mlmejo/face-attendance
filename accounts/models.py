from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user: User = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Email address',
        max_length=255,
        unique=True
    )
    is_admin = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perm(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
