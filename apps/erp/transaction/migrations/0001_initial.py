# Generated by Django 3.2.5 on 2024-03-16 04:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('payment', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaleTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', model_utils.fields.AutoCreatedField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Criado em')),
                ('updated_at', model_utils.fields.AutoLastModifiedField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Modificado em')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('sale_transaction_status', models.CharField(choices=[('creation', 'Order Creation'), ('billing', 'Billing'), ('payment_pending', 'Payment Pending'), ('payment_processing', 'Payment Processing'), ('payment_approved', 'Payment Approved'), ('payment_denied', 'Payment Denied'), ('cancelled', 'Cancelled'), ('returned', 'Returned'), ('refunded', 'Refunded')], default='creation', max_length=20, verbose_name='Status')),
                ('sale_transaction_type', models.CharField(choices=[('expense', 'Expense'), ('revenue', 'Revenue')], default='expense', max_length=10, verbose_name='Sale Transaction Type')),
                ('total_quantity', models.PositiveIntegerField(default=0, null=True, verbose_name='Total Quantity')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Total Amount')),
                ('total_discount_amount', models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Total Discount Amount')),
                ('net_amount', models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Net Amount')),
                ('tax_amount', models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Tax Amount')),
                ('total_due', models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Total Due')),
                ('sale_date', models.DateTimeField(null=True, verbose_name='Sale Date')),
                ('customer', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.customer', verbose_name='Customer')),
                ('seller', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sale_transaction_seller', to=settings.AUTH_USER_MODEL, verbose_name='Seller')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Sale Transaction',
                'verbose_name_plural': 'Sales Transactions',
                'db_table': 'sale_transaction',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', model_utils.fields.AutoCreatedField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Criado em')),
                ('updated_at', model_utils.fields.AutoLastModifiedField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Modificado em')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Paid', 'Paid'), ('Cancelled', 'Cancelled')], default='Pending', max_length=20, verbose_name='Transaction Status')),
                ('type_transaction', models.CharField(choices=[('sale', 'Sale')], max_length=4, verbose_name='Transaction Type')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total Amount')),
                ('total_discount_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total Discount Amount')),
                ('net_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Net Amount')),
                ('notes', models.TextField(blank=True, verbose_name='Notes')),
            ],
            options={
                'verbose_name': 'Transaction',
                'verbose_name_plural': 'Transactions',
                'db_table': 'transaction',
            },
        ),
        migrations.CreateModel(
            name='SaleTransactionPaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', model_utils.fields.AutoCreatedField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Criado em')),
                ('updated_at', model_utils.fields.AutoLastModifiedField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Modificado em')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('payment_date', models.DateTimeField(auto_now_add=True, help_text='Date and time the payment was registered.', verbose_name='Payment Date')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Total Amount')),
                ('name_card_holder', models.CharField(blank=True, help_text='Issuing bank for checks or bank transfers.', max_length=50, verbose_name='Issuing Bank')),
                ('issuing_bank', models.CharField(blank=True, help_text='Issuing bank for checks or bank transfers.', max_length=50, verbose_name='Issuing Bank')),
                ('number', models.CharField(blank=True, help_text='Check or card number.', max_length=20, verbose_name='Number')),
                ('installment', models.IntegerField(blank=True, default=0, max_length=3, null=True, verbose_name='Installments')),
                ('validity', models.DateField(blank=True, help_text='Card validity date, if applicable.', null=True, verbose_name='Validity')),
                ('payer_cpf_cnpj', models.CharField(blank=True, help_text='Payer’s CPF or CNPJ for PIX or boletos.', max_length=14, verbose_name='Payer CPF/CNPJ')),
                ('pix_key', models.CharField(blank=True, help_text='PIX key for payments via PIX.', max_length=255, verbose_name='PIX Key')),
                ('e_wallet_provider', models.CharField(blank=True, help_text='Provider of the E-Wallet, if applicable.', max_length=50, verbose_name='E-Wallet Provider')),
                ('payment_method', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='payment.paymentmethod', verbose_name='')),
                ('sale_transaction', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payment_methods', to='transaction.saletransaction', verbose_name='')),
            ],
            options={
                'verbose_name': 'Payment of Sale Transaction Installment',
                'verbose_name_plural': 'Payments of Sale Transaction Installments',
                'db_table': 'sale_transaction_payment_method',
            },
        ),
        migrations.CreateModel(
            name='SaleTransactionPaymentInstallment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', model_utils.fields.AutoCreatedField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Criado em')),
                ('updated_at', model_utils.fields.AutoLastModifiedField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Modificado em')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Paid', 'Paid'), ('Cancelled', 'Cancelled')], default='Pending', max_length=10, verbose_name='Status')),
                ('total_installments', models.PositiveIntegerField(blank=True, null=True, verbose_name='Installment Total')),
                ('installment', models.PositiveIntegerField(blank=True, null=True, verbose_name='Installment Number')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Total Amount')),
                ('total_discount_amount', models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Total Discount Amount')),
                ('net_amount', models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Net Amount')),
                ('tax_amount', models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Tax Amount')),
                ('notes', models.TextField(blank=True, verbose_name='Notes')),
                ('payment_method', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='payment.paymentmethod', verbose_name='Payment Method')),
                ('sale_transaction', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payment_installments', to='transaction.saletransaction', verbose_name='Sale Transaction')),
                ('sale_transaction_payment_method', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payment_method_installment', to='transaction.saletransactionpaymentmethod', verbose_name='Sale Transaction Payment Method')),
            ],
            options={
                'verbose_name': 'Payment of Sale Transaction Installment',
                'verbose_name_plural': 'Payments of Sale Transaction Installments',
                'db_table': 'sale_transaction_payment_installment',
            },
        ),
        migrations.CreateModel(
            name='SaleTransactionItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', model_utils.fields.AutoCreatedField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Criado em')),
                ('updated_at', model_utils.fields.AutoLastModifiedField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Modificado em')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Quantity')),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Sale Price')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Total Amount')),
                ('discount', models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Discount')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='Product')),
                ('sale_transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='transaction.saletransaction', verbose_name='Sale')),
            ],
            options={
                'verbose_name': 'Sale Item',
                'verbose_name_plural': 'Sale Items',
                'db_table': 'sale_item',
            },
        ),
    ]
