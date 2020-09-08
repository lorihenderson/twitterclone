from django.shortcuts import render, HttpResponseRedirect, reverse
from tweet.models import Tweet
from tweet.forms import AddTweet
from django.contrib.auth.decorators import login_required
from notification.models import Notification
from twitteruser.models import TwitterUser
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
import re


@login_required
def tweet_index(request):
    my_tweets = Tweet.objects.filter(tweet_author=request.user)
    following_list = Tweet.objects.filter(tweet_author__in=request.user.following.all())
    feed = my_tweets | following_list
    feed = feed.order_by("-time_date")
    notifications = Notification.objects.filter(recipient__id=request.user.id, viewed=False)
    return render(request, "index.html", {"my_tweets": my_tweets, "following_list": following_list, "feed": feed, "notification_count": len(notifications)})


class TweetDetailView(TemplateView):
    def get(self, request, tweet_id):
        html = "tweet_detail.html"
        my_tweet = Tweet.objects.filter(id=tweet_id).first()
        return render(request, html, {"my_tweet": my_tweet})


class AddTweetView(TemplateView):
    def get(self, request):
        form = AddTweet()
        return render(request, "generic_form.html", {"form": form})

    def post(self, request):
        form = AddTweet(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            notify_user = re.findall(r"@([\w]+)", data.get("tweet_post"))
            new_tweet = Tweet.objects.create(
                tweet_post = data.get("tweet_post"),
                tweet_author = request.user
            )
            if notify_user:
                for notified in notify_user:
                    notification_tweet = Notification.objects.create(
                        tweet_received = new_tweet,
                        recipient = TwitterUser.objects.get(username=notified)
                    )
            return HttpResponseRedirect(reverse("homepage"))
        else:
            return render(request, "generic_form.html", {"form": form})