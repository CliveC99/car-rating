# Generated by Django 4.2.4 on 2023-08-26 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_contact_email_alter_contact_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.TextField(default='VAG'),
        ),
    ]
