# Generated by Django 4.2.1 on 2023-05-08 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_customer_active_organization_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='some_big_int_val',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='some_date_val',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='some_float_val',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='some_uniqueidentifier_val',
            field=models.UUIDField(null=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='some_utc_date_time_val',
            field=models.DateTimeField(null=True),
        ),
    ]
