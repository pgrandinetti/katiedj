from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class TrafficUserManager(BaseUserManager):
    def create_user(self, email, public_name, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            public_name=public_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, public_name, password):
        user = self.create_user(
            email,
            public_name=public_name,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class TrafficUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = TrafficUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['public_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def get_short_name(self):
        return self.email

    def get_full_name(self):
        return "{}".format(self.email)

    def email_user(self, *args, **kwargs):
        send_mail(
            '{}'.format(args[0]),
            '{}'.format(args[1]),
            settings.EMAIL_DEFAULT_SENDER,
            [self.email],
            fail_silently=False,
        )

    def can_login(self):
        return self.is_active
