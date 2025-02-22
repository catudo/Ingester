from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser

class Comments(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    url = models.URLField()
    score = models.DecimalField(decimal_places=2,max_digits=10)
    author = models.CharField(max_length=100)
    subreddit = models.CharField(max_length=100)
    created_utc = models.DateTimeField()
    subject = models.CharField(max_length=100)
    sentiment = models.CharField(max_length=10)
    sentiment_score = models.DecimalField(decimal_places=2,max_digits=10)
    user = models.CharField(max_length=100)

    class Meta:
        db_table = 'comments'


class UserManager(BaseUserManager):

    use_in_migration = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is Required')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')

        return self.create_user(email, password, **extra_fields)

class UserApi(AbstractUser):
    username = None
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []



    def __str__(self):
        return self.name
