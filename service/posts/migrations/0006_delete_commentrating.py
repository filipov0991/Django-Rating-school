# Generated by Django 4.1.7 on 2023-04-04 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_commentrating_score'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CommentRating',
        ),
    ]
