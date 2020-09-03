from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from twitteruser.models import TwitterUser
from tweet.models import Tweet

admin.site.register(Tweet)