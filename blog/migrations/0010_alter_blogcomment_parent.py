# Generated by Django 3.2.7 on 2021-10-14 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_blogcomment_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='parent',
            field=models.IntegerField(default=0, null=True),
        ),
    ]