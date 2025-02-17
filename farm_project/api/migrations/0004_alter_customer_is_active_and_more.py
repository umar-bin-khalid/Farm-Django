# Generated by Django 4.2.1 on 2023-05-08 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_customer_insert_user_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='is_active',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='is_email_allowed',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='is_email_confirmed',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='is_email_marketing_allowed',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='is_locked',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='is_multiple_organizations_allowed',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='is_verbose_logging_forced',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='customerrole',
            name='is_placeholder',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='customerrole',
            name='placeholder',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='dategreaterthanfilter',
            name='is_active',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='errorlog',
            name='is_client_side_error',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='errorlog',
            name='is_resolved',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='flavor',
            name='is_active',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='is_active',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='orgApiKey',
            name='is_active',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='orgApiKey',
            name='is_temp_user_key',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='pac',
            name='display_order',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pac',
            name='is_active',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='is_delete_allowed',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='is_edit_allowed',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='some_bit_val',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='is_active',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='tac',
            name='is_active',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='tristatefilter',
            name='display_order',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='tristatefilter',
            name='is_active',
            field=models.BooleanField(null=True),
        ),
    ]
