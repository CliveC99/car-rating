# Generated by Django 4.2.4 on 2023-08-25 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_contact_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='post',
        ),
    ]
