# Generated by Django 4.1.6 on 2023-02-25 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_entry_is_deleted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='is_deleted',
        ),
    ]
