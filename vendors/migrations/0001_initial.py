# Generated by Django 3.2.7 on 2024-01-11 21:03

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('frontend', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Ημερομηνια')),
                ('title', models.CharField(max_length=150, verbose_name='Αριθμος Τιμολογιου')),
                ('value', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Καθαρή Αξια')),
                ('extra_value', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='ΜΕΤΑΦΟΡΙΚΑ')),
                ('final_value', models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='Αξία')),
                ('description', models.TextField(blank=True, verbose_name='Λεπτομεριες')),
                ('taxes_6', models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='ΠΟΣΟ ΦΠΑ 6%')),
                ('taxes_13', models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='ΠΟΣΟ ΦΠΑ 13%')),
                ('taxes_24', models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='ΠΟΣΟ ΦΠΑ 24%')),
                ('payment_method', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='frontend.paymentmethod', verbose_name='Τροπος Πληρωμης')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='Ενεργό')),
                ('job_description', models.TextField(blank=True, null=True, verbose_name='ΕΠΑΓΓΕΛΜΑ')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='Εταιρία')),
                ('identifier', models.IntegerField(blank=True, null=True, verbose_name='Αριθμος Προϊόντων')),
                ('owner', models.CharField(blank=True, max_length=200, verbose_name='Ιδιοκτήτης')),
                ('afm', models.CharField(blank=True, max_length=150, verbose_name='ΑΦΜ')),
                ('doy', models.CharField(blank=True, max_length=150, verbose_name='ΔΟΥ')),
                ('phone', models.CharField(blank=True, max_length=200, verbose_name='Σταθερο Τηλεφωνο')),
                ('cellphone', models.CharField(blank=True, max_length=200, verbose_name='Κινητό')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('site', models.URLField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Λεπτομεριες')),
                ('address', models.CharField(blank=True, max_length=240, null=True, verbose_name='Διευθυνση')),
                ('city', models.CharField(blank=True, max_length=240, null=True, verbose_name='Πολη')),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=50, verbose_name='Υπόλοιπο')),
                ('paid_value', models.DecimalField(decimal_places=2, default=0.0, max_digits=50)),
                ('value', models.DecimalField(decimal_places=2, default=0.0, max_digits=50)),
                ('taxes_modifier', models.CharField(choices=[('a', 0), ('d', 6), ('b', 13), ('c', 24)], default='c', max_length=1)),
            ],
            options={
                'ordering': ['identifier', 'title'],
            },
        ),
        migrations.CreateModel(
            name='VendorBankingAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, verbose_name='Ονομα Δικαιούχου')),
                ('iban', models.CharField(blank=True, max_length=150)),
                ('code', models.CharField(blank=True, max_length=200, verbose_name='Αριθμός Λογαριασμού')),
                ('payment_method', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='banking_accounts', to='frontend.paymentmethod', verbose_name='Τροπος Πληρωμής')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bankings', to='vendors.vendor', verbose_name='Προμηθευτής')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Ημερομηνία')),
                ('title', models.CharField(max_length=150, verbose_name='Τίτλος')),
                ('value', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Αξία')),
                ('description', models.TextField(blank=True, verbose_name='Περιγραφή')),
                ('payment_method', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='frontend.paymentmethod', verbose_name='Τροπος Πληρωμής')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='vendors.vendor', verbose_name='Προμηθευτής')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Paycheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('edited', models.DateField(auto_now=True)),
                ('title', models.CharField(blank=True, max_length=240, verbose_name='ΠΕΡΙΓΡΑΦΗ')),
                ('date', models.DateField(verbose_name='ΗΜΕΡΟΜΗΝΙΑ')),
                ('is_done', models.BooleanField(default=False, verbose_name='ΟΛΟΚΛΗΡΩΜΕΝΗ')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='ΠΟΣΟ')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendors.vendor', verbose_name='ΠΡΟΜΗΘΕΥΤΗΣ')),
            ],
            options={
                'ordering': ['is_done', 'date'],
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True, verbose_name='Κατάσταση')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('text', tinymce.models.HTMLField(blank=True)),
                ('vendor_related', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='vendors.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Ημερομηνια')),
                ('order_code', models.CharField(blank=True, max_length=50, null=True, verbose_name='Κωδικος Τιμολογιου')),
                ('unit', models.CharField(choices=[('a', 'Τεμάχιο'), ('b', 'Κιβώτιο'), ('c', 'Κιλό')], default='a', max_length=1, verbose_name='ΜΜ')),
                ('qty', models.DecimalField(decimal_places=2, default=1, max_digits=17, verbose_name='Ποσότητα')),
                ('value', models.DecimalField(decimal_places=2, max_digits=17, verbose_name='Τιμή Μοναδας')),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Εκπτωση')),
                ('discount_value', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Ποσο Εκπτωσης')),
                ('clean_value', models.DecimalField(decimal_places=2, max_digits=17, verbose_name='Αξια')),
                ('total_clean_value', models.DecimalField(decimal_places=2, max_digits=17, verbose_name='Καθαρη Αξια')),
                ('taxes_modifier', models.CharField(choices=[('a', 0), ('d', 6), ('b', 13), ('c', 24)], default='c', max_length=1)),
                ('taxes_value', models.DecimalField(decimal_places=2, max_digits=17, verbose_name='Αξια ΦΠΑ')),
                ('extra_value', models.DecimalField(decimal_places=2, max_digits=17, verbose_name='Αξια Μεταφορικων')),
                ('total_value', models.DecimalField(decimal_places=2, max_digits=17, verbose_name='Τελικη Αξία')),
                ('final_value_unit', models.DecimalField(decimal_places=2, default=0, max_digits=17, verbose_name='Τελικη Αξία')),
                ('used_qty', models.DecimalField(decimal_places=2, default=0, max_digits=17)),
                ('remaining_qty', models.DecimalField(decimal_places=2, default=0, max_digits=17)),
                ('remaining_total_cost', models.DecimalField(decimal_places=2, default=0, max_digits=17)),
                ('income_percent', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='vendors.invoice')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='invoice_vendor_items', to='products.product', verbose_name='Προϊον')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vendors.vendor', verbose_name='Προμηθευτης')),
            ],
            options={
                'ordering': ['-date', 'id'],
            },
        ),
        migrations.AddField(
            model_name='invoice',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='vendors.vendor', verbose_name='Προμηθευτης'),
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=200, verbose_name='Ονομασια')),
                ('phone', models.CharField(blank=True, max_length=10, verbose_name='Τηλεφωνο')),
                ('cellphone', models.CharField(blank=True, max_length=10, verbose_name='Κινητο')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='persons', to='vendors.vendor', verbose_name='Προμηθευτης')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
