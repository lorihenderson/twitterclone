from django.shortcuts import render, HttpResponseRedirect, reverse
from notification.models import Notification


def show_notifications(request, notification_id):
    notifications = Notification.objects.filter(recipient__id=notification_id)
    notification_list = []
    for notify in notifications:
        if not notify.viewed:
            notification_list.append(notify.tweet_received)
        notify.viewed = True
        notify.save()
    return render(request, "notifications.html", {"notifications": notification_list})