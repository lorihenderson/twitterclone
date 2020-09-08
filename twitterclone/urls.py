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
from twitteruser.views import signup_view, author_detail, following_view, unfollowing_view
from authentication.views import login_view, logout_view
from tweet.views import tweet_index, add_tweet, tweet_detail
from notification.views import show_notifications



urlpatterns = [
    path('', tweet_index, name = "homepage"),
    path('login/', login_view),
    path('logout/', logout_view),
    path('signup/', signup_view),
    path('addtweet/', add_tweet),
    path('tweet_post/<int:tweet_id>/', tweet_detail),
    path('tweet_author/<int:author_id>/', author_detail),
    path('following/<int:follow_id>/', following_view),
    path('unfollowing/<int:unfollow_id>/', unfollowing_view),
    path('notification/<int:notification_id>/', show_notifications),
    path('admin/', admin.site.urls),
]
