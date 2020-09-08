"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from twitteruser.views import SignupView, AuthorDetailView, FollowingView, UnfollowingView
from authentication.views import login_view, logout_view
from tweet.views import tweet_index, AddTweetView, TweetDetailView
from notification.views import show_notifications


urlpatterns = [
    path('', tweet_index, name = "homepage"),
    path('login/', login_view),
    path('logout/', logout_view),
    path('signup/', SignupView.as_view()),
    path('addtweet/', AddTweetView.as_view()),
    path('tweet_post/<int:tweet_id>/', TweetDetailView.as_view()),
    path('tweet_author/<int:author_id>/', AuthorDetailView.as_view()),
    path('following/<int:follow_id>/', FollowingView.as_view()),
    path('unfollowing/<int:unfollow_id>/', UnfollowingView.as_view()),
    path('notification/<int:notification_id>/', show_notifications),
    path('admin/', admin.site.urls),
]
