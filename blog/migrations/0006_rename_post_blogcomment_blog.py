# Generated by Django 3.2.7 on 2021-10-14 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blogcomment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogcomment',
            old_name='post',
            new_name='blog',
        ),
    ]