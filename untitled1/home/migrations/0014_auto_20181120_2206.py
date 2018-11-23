# Generated by Django 2.1.3 on 2018-11-20 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20181120_1956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='faculty',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='studentid',
        ),
        migrations.RemoveField(
            model_name='student',
            name='status',
        ),
        migrations.AddField(
            model_name='student',
            name='issue',
            field=models.CharField(default='NULL', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='subject',
            field=models.CharField(default='NULL', max_length=100),
        ),
        migrations.DeleteModel(
            name='issue',
        ),
    ]