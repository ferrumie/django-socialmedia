# Generated by Django 3.1 on 2020-09-06 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20200907_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
