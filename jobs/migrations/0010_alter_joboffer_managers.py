# Generated by Django 3.2.6 on 2021-08-23 09:29

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_alter_joboffer_company'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='joboffer',
            managers=[
                ('enabled', django.db.models.manager.Manager()),
            ],
        ),
    ]
