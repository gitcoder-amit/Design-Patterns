from django.db import models

class RecipeManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted = False)

class Recipe(models.Model):
    name = models.CharField(max_length = 30)
    description = models.TextField(max_length = 30)
    objects = RecipeManager()
    admin_objects = models.Manager()

    class Meta:
        indexes = [models.Index(fields = ['name', 'description']]



# users/models.py
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, AbstractUser

class UserManager(BaseUserManager):
    def create_user(self, name, phone_number, email=None, password=None, **extra_fields):
        if not name:
            raise ValueError('The Name field is required')
        if not phone_number:
            raise ValueError('The Phone Number field is required')
        
        user = self.model(
            name=name,
            phone_number=phone_number,
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, phone_number, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        user = self.create_user(
            name=name,
            phone_number=phone_number,
            email=email,
            password=password,
            **extra_fields,
        )
        return user


class CustomUser(AbstractUser):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    username = None
    first_name = None
    last_name = None


    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return str(self.id)