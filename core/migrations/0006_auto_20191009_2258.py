# Generated by Django 2.2.6 on 2019-10-09 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_test_memo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='kakao_user_id',
            field=models.CharField(max_length=150),
        ),
    ]
