# Generated by Django 3.2.7 on 2021-10-10 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20211010_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.CharField(default='', max_length=50),
        ),
    ]
