# Generated by Django 3.2.7 on 2021-10-14 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20211014_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='reply',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
