# Generated by Django 4.2.4 on 2023-08-25 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.post'),
        ),
    ]
