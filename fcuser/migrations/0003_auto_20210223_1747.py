# Generated by Django 3.1.6 on 2021-02-23 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fcuser', '0002_auto_20210223_1734'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fcuser',
            old_name='username1',
            new_name='useremail',
        ),
    ]