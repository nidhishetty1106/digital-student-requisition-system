# Generated by Django 2.1.3 on 2018-11-23 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20181122_1253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='facid',
        ),
    ]
