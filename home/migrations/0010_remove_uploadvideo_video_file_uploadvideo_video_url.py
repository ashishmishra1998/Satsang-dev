# Generated by Django 4.0.5 on 2022-06-30 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_about_us_content_customer_reviews_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadvideo',
            name='video_file',
        ),
        migrations.AddField(
            model_name='uploadvideo',
            name='video_url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
