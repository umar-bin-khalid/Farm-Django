# Generated by Django 4.2.1 on 2023-05-08 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_customer_email_confirmed_utc_date_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='fs_user_code_value',
            field=models.UUIDField(null=True),
        ),
        migrations.AlterField(
            model_name='errorlog',
            name='browser_code',
            field=models.UUIDField(null=True),
        ),
        migrations.AlterField(
            model_name='errorlog',
            name='context_code',
            field=models.UUIDField(null=True),
        ),
    ]
