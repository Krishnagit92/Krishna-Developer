# Generated by Django 5.1.5 on 2025-01-29 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer_register_table',
            name='otp_number',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
