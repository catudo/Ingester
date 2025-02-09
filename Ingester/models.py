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




class UserApi(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',  # Change this name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # Change this name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
