# Generated by Django 3.1.6 on 2021-02-23 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcuser', '0004_remove_fcuser_useremail'),
    ]

    operations = [
        migrations.AddField(
            model_name='fcuser',
            name='useremail',
            field=models.EmailField(default='gksxogh33@naver.com', max_length=128, verbose_name='사용자이메일'),
            preserve_default=False,
        ),
    ]
