# Generated by Django 3.2.7 on 2021-10-15 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_blogcomment_parent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogcomment',
            old_name='parent',
            new_name='parent_comment_id',
        ),
    ]