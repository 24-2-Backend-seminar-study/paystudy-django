# Generated by Django 4.2.8 on 2024-07-07 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kakaopay', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kakaopay',
            name='user',
        ),
    ]