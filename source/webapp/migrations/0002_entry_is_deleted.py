# Generated by Django 4.1.6 on 2023-02-25 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='удалено'),
        ),
    ]