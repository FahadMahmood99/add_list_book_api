# Generated by Django 5.1 on 2024-10-29 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='link',
        ),
    ]
