from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from twitteruser.models import TwitterUser
from tweet.models import Tweet
from twitteruser.forms import SignupForm


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = TwitterUser.objects.create_user(
                username=data.get("username"),
                password=data.get("password"),
            )
            if new_user:
                login(request, new_user)
                return HttpResponseRedirect(reverse("homepage"))

    form = SignupForm()
    return render(request, "generic_form.html", {"form": form})


def author_detail(request, author_id):
    current_user = TwitterUser.objects.filter(id=author_id).first()
    tweet_grabber = Tweet.objects.filter(tweet_author=current_user)
    return render(request, "author_detail.html", {"current_user": current_user, "tweet_grabber": tweet_grabber})


def following_view(request, follow_id):
    signed_in_user = TwitterUser.objects.filter(username=request.user.username).first()
    follow = TwitterUser.objects.filter(id=follow_id).first()
    signed_in_user.following.add(follow)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def unfollowing_view(request, unfollow_id):
    signed_in_user = request.user
    unfollow = TwitterUser.objects.filter(id=unfollow_id).first()
    signed_in_user.following.remove(unfollow)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
