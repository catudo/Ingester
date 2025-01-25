from django.db import models

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
