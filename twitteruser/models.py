from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class TwitterUser(AbstractUser):
    following = models.ManyToManyField("self", symmetrical=False)
# followers