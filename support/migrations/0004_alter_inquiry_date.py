# Generated by Django 3.2.3 on 2022-05-03 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0003_auto_20220503_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='생성일시'),
        ),
    ]
