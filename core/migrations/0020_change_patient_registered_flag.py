# Generated by Django 2.2.6 on 2019-11-04 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_add_code_to_hospital'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='registered_flag',
        ),
        migrations.AddField(
            model_name='patient',
            name='register_completed_flag',
            field=models.BooleanField(default=False, verbose_name='계정 등록 완료 여부'),
        ),
    ]
