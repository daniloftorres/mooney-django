# Generated by Django 3.2.5 on 2024-03-11 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0004_alter_paymentinstallmentsaletransaction_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentinstallmentsaletransaction',
            name='installment',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Installment Number'),
        ),
    ]