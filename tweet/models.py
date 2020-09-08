from django.db import models
from django.utils import timezone
from twitteruser.models import TwitterUser

class Tweet(models.Model):
    tweet_post = models.TextField(max_length=140)
    time_date = models.DateTimeField(default=timezone.now)
    tweet_author = models.ForeignKey(TwitterUser, on_delete=models.CASCADE, related_name="tweetauthor")
