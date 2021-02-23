# Generated by Django 3.1.6 on 2021-02-23 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fcuser',
            name='username1',
            field=models.EmailField(default='gksxogh33@naver.com', max_length=128, verbose_name='사용자이메일'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fcuser',
            name='username',
            field=models.CharField(max_length=32, verbose_name='사용자명'),
        ),
    ]
