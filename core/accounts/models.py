from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, AbstractUser


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError("Email is required.")
        if not username:
            raise ValueError("Username is required.")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_verified", True)

        if not extra_fields.get("is_superuser"):
            raise ValueError("superuser must be true.")
        if not extra_fields.get("is_active"):
            raise ValueError("is active must be true")
        if not extra_fields.get("is_staff"):
            raise ValueError("is staff must be true")
        if not extra_fields.get("is_verified"):
            raise ValueError("is verified must be true")

        return self.create_user(email, username, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=128)
    email = models.EmailField(unique=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = "username"

    objects = CustomUserManager()

    def __str__(self):
        return self.username


class Profile(models.Model):
    first_name = models.CharField(max_length=128, blank=True, null=True)
    last_name = models.CharField(max_length=128,blank=True, null=True)
    bio = models.TextField()
    avatar = models.ImageField(upload_to='profile_images')
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"
