from django.db import models
from twitteruser.models import TwitterUser
from tweet.models import Tweet


class Notification(models.Model):
    recipient = models.ForeignKey(TwitterUser, on_delete=models.CASCADE, related_name="recipient_user")
    tweet_received = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name="tweetreceived")
    viewed = models.BooleanField(default=False)