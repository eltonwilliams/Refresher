# Generated by Django 2.0.7 on 2018-08-23 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testboxes', '0003_uat_prefix'),
    ]

    operations = [
        migrations.AddField(
            model_name='uat',
            name='running',
            field=models.BooleanField(default=False),
        ),
    ]
