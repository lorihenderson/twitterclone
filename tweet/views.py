from django.shortcuts import render, HttpResponseRedirect, reverse
from tweet.models import Tweet
from tweet.forms import AddTweet
from django.contrib.auth.decorators import login_required


@login_required
def tweet_index(request):
    my_tweets = Tweet.objects.all()
    return render(request, "index.html", {"my_tweets": my_tweets})


def tweet_detail(request, tweet_id):
    my_tweet = Tweet.objects.filter(id=tweet_id).first()
    return render(request, "tweet_detail.html", {"my_tweet": my_tweet})


def add_tweet(request):
    if request.method == "POST":
        form = AddTweet(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Tweet.objects.create(
                tweet = data.get("tweet"),
                tweet_author = request.user
            )
            return HttpResponseRedirect(reverse("homepage"))

    form = AddTweet()
    return render(request, "generic_form.html", {"form": form})