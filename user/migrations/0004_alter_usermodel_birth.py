# Generated by Django 5.1.4 on 2024-12-16 11:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_usermodel_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='birth',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 16, 16, 19, 26, 684302)),
        ),
    ]