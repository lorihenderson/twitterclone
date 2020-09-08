# Generated by Django 3.0.1 on 2020-09-05 18:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet_post', models.TextField(max_length=140)),
                ('time_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
