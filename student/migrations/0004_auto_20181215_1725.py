# Generated by Django 2.1 on 2018-12-15 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20181215_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisitions',
            name='issue',
            field=models.TextField(max_length=20),
        ),
        migrations.AlterField(
            model_name='requisitions',
            name='office_section',
            field=models.TextField(max_length=20),
        ),
        migrations.AlterField(
            model_name='requisitions',
            name='reason',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='requisitions',
            name='subject',
            field=models.TextField(max_length=50),
        ),
    ]
