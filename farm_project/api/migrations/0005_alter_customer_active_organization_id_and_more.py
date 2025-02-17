# Generated by Django 4.2.1 on 2023-05-08 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_customer_is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='active_organization_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='tac_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='utc_offset_in_minutes',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='dategreaterthanfilter',
            name='day_count',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='dategreaterthanfilter',
            name='display_order',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='flavor',
            name='display_order',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='display_order',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='some_int_val',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='display_order',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='tac',
            name='display_order',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='tristatefilter',
            name='state_int_value',
            field=models.IntegerField(null=True),
        ),
    ]
