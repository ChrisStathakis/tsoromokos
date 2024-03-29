# Generated by Django 3.2.7 on 2024-01-11 21:03

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Costumer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eponimia', models.CharField(max_length=240, null=True, verbose_name='Επωνυμια')),
                ('address', models.CharField(blank=True, max_length=240, null=True, verbose_name='Διευθυνση')),
                ('city', models.CharField(blank=True, max_length=220, null=True, verbose_name='πολη')),
                ('job_description', models.CharField(blank=True, max_length=240, null=True, verbose_name='Επαγγελμα')),
                ('loading_place', models.CharField(blank=True, default='Εδρα μας', max_length=240, null=True, verbose_name='Τόπος Φόρτωσης')),
                ('destination', models.CharField(blank=True, default='Εδρα του,', max_length=240, null=True, verbose_name='Προορισμος')),
                ('afm', models.CharField(blank=True, max_length=10, null=True, verbose_name='ΑΦΜ')),
                ('doy', models.CharField(blank=True, default='Σπαρτη', max_length=240, null=True, verbose_name='ΔΟΥ')),
                ('destination_city', models.CharField(blank=True, max_length=240, null=True, verbose_name='ΤΟΠΟΣ ΠΡΟΟΡΙΣΜΟΥ')),
                ('transport', models.CharField(blank=True, max_length=10, null=True, verbose_name='Μεταφορικό Μέσο')),
                ('first_name', models.CharField(blank=True, max_length=200, verbose_name='Ονομα')),
                ('last_name', models.CharField(blank=True, max_length=200, verbose_name='Επιθετο')),
                ('amka', models.CharField(blank=True, max_length=200, verbose_name='Ψευδονυμο')),
                ('notes', models.CharField(blank=True, max_length=200, verbose_name='Σημειώσεις')),
                ('cellphone', models.CharField(blank=True, max_length=200, verbose_name='Κινητό')),
                ('phone', models.CharField(blank=True, max_length=200, null=True, verbose_name='Τηλέφωνο')),
                ('active', models.BooleanField(default=True, verbose_name='Ενεργός')),
                ('value', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('paid_value', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
            ],
            options={
                'ordering': ['eponimia', 'afm'],
            },
        ),
        migrations.CreateModel(
            name='CostumerDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eponimia', models.CharField(max_length=240, null=True, verbose_name='Επωνυμια')),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('address', models.CharField(blank=True, max_length=240, null=True, verbose_name='Διευθυνση')),
                ('job_description', models.CharField(blank=True, max_length=240, null=True, verbose_name='Επαγγελμα')),
                ('loading_place', models.CharField(blank=True, default='Εδρα μας', max_length=240, null=True, verbose_name='Τοπος Φορτωσης')),
                ('destination', models.CharField(blank=True, default='Εδρα του,', max_length=240, null=True, verbose_name='Προορισμος')),
                ('afm', models.CharField(blank=True, max_length=10, null=True, verbose_name='ΑΦΜ')),
                ('doy', models.CharField(blank=True, default='Σπαρτη', max_length=240, null=True, verbose_name='ΔΟΥ')),
                ('destination_city', models.CharField(blank=True, max_length=240, null=True, verbose_name='Πολη')),
                ('transport', models.CharField(blank=True, max_length=10, null=True, verbose_name='Μεταφορικο Μεσο')),
                ('phone', models.CharField(blank=True, max_length=200, null=True, verbose_name='Τηλεφωνα')),
                ('purpose_of_another_movement', models.CharField(blank=True, max_length=220, null=True, verbose_name='ΣΚΟΠΟΣ ΑΛΛΗΣ ΔΙΑΚΙΝΗΣΗΣ')),
            ],
        ),
        migrations.CreateModel(
            name='MyCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite', models.BooleanField(default=False, verbose_name='Προτεινομενο')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='Τιτλος')),
                ('eponimia', models.CharField(blank=True, max_length=200, verbose_name='Επωνυμια')),
                ('job', models.TextField(blank=True, verbose_name='Περιγραφη Επαγγελματος')),
                ('afm', models.CharField(blank=True, max_length=10, verbose_name='ΑΦΜ')),
                ('doy', models.CharField(blank=True, max_length=150, verbose_name='ΔΟΥ')),
                ('city', models.CharField(blank=True, max_length=150, verbose_name='Εδρα')),
                ('zipcode', models.CharField(blank=True, max_length=10, verbose_name='TK')),
                ('phone', models.CharField(blank=True, max_length=100, verbose_name='Τηλεφωνα')),
                ('fax', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentInvoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(blank=True, max_length=40, null=True, verbose_name='Αναγνωριστικό Παραστατικού')),
                ('mark', models.TextField(blank=True, null=True, verbose_name='Μοναδικός Αριθμός Καταχώρησης Παραστατικού')),
                ('authenticationCode', models.CharField(blank=True, max_length=240, null=True, verbose_name='Συμβολοσειρά Αυθεντικοποίησης')),
                ('locked', models.BooleanField(default=False, verbose_name='Κλειδωμενο')),
                ('payment_info', models.CharField(choices=[('1', 'Λογαριασμός Πληρωμών Ημεδαπής'), ('2', 'E-Banking Αρ. Λογ. Πάροχος Πληρωμών'), ('3', 'E-Pos Αρ. Λογ. Πάροχος Πληρωμών'), ('4', 'Κατάθεση Αρ. Λογ. Πάροχος Πληρωμών'), ('5', 'Λογαριασμός Πληρωμών Αλλοδαπής'), ('6', 'E-Banking Αρ. Λογ. Πάροχος Πληρωμών'), ('7', 'E-Pos Αρ. Λογ. Πάροχος Πληρωμών'), ('8', 'Κατάθεση Αρ. Λογ. Πάροχος Πληρωμών'), ('9', 'Μετρητά')], default='9', max_length=3)),
                ('order_type', models.CharField(choices=[('1.1', 'Τιμολόγιο - Δελτίο Αποστολής'), ('2.1', 'Τιμολόγιο Παροχής'), ('c', 'Προπαραγγελια'), ('d', 'Δελτίο Αποστολής')], default=1.1, max_length=3, verbose_name='Ειδος Παραστατικου')),
                ('number', models.IntegerField(blank=True, null=True)),
                ('series', models.CharField(choices=[('a', 'A'), ('b', 'Δοκιμαστικο')], max_length=1, verbose_name='ΣΕΙΡΑ')),
                ('place', models.CharField(blank=True, max_length=220, verbose_name='ΤΟΠΟΣ ΕΚΔΟΣΗΣ')),
                ('date', models.DateTimeField(default=datetime.datetime(2024, 1, 11, 21, 3, 49, 745124, tzinfo=utc), verbose_name='ΗΜΕΡΟΜΗΝΙΑ')),
                ('delivery_time', models.CharField(blank=True, max_length=220, null=True, verbose_name='ΩΡΑ ΠΑΡΑΔΟΣΗΣ')),
                ('writing_qty', models.TextField(blank=True, null=True, verbose_name='ΠΟΣΟΤΗΤΑ ΟΛΟΓΡΑΦΩΣ')),
                ('number_of_invoice', models.CharField(blank=True, max_length=100, null=True, verbose_name='ΑΡΙΘΜΟΣ ΣΧΕΤΙΚΟΥ ΠΑΡΑΣΤΑΤΙΚΟΥ')),
                ('purpose_of_moving', models.CharField(blank=True, choices=[('1', 'Πώληση'), ('2', 'Πώληση για Λογαριασμό Τρίτων'), ('a', 'Δειγματισμός')], default=1, max_length=1, null=True, verbose_name='Σκοπός Διακίνησης')),
                ('discount_value', models.DecimalField(decimal_places=2, default=0.0, max_digits=17, verbose_name='Εκπτωση')),
                ('clean_value', models.DecimalField(decimal_places=2, default=0.0, max_digits=17, verbose_name='Καθαρη Αξια')),
                ('taxes_value', models.DecimalField(decimal_places=2, default=0.0, max_digits=17, verbose_name='Συνολο ΦΠΑ')),
                ('charges_cost', models.DecimalField(decimal_places=2, default=0.0, max_digits=17, verbose_name='επιβαρυνσεις')),
                ('charges_taxes', models.DecimalField(decimal_places=2, default=0.0, max_digits=17, verbose_name='επιβαρυνσεις ΦΠΑ')),
                ('total_value', models.DecimalField(decimal_places=2, default=0, max_digits=17, verbose_name='Πληρωτεο Ποσο')),
                ('final_value', models.DecimalField(decimal_places=2, default=0, max_digits=17, verbose_name='Τελική Αξία')),
                ('old_balance', models.DecimalField(decimal_places=2, default=0, max_digits=17, verbose_name='Προηγούμενο')),
                ('new_balance', models.DecimalField(decimal_places=2, default=0, max_digits=17, verbose_name='Νέο')),
                ('notes', models.TextField(blank=True, null=True)),
                ('card_info', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='costumers.mycard', verbose_name='Στάμπα')),
                ('costumer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='payment_invoices', to='costumers.costumer', verbose_name='Πελάτης')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='InvoiceItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=250, verbose_name='Περιγραφη')),
                ('unit', models.CharField(choices=[('a', 'Τεμάχιο'), ('b', 'Κιβώτιο'), ('c', 'Κιλό')], default='a', max_length=1, verbose_name='ΜΜ')),
                ('qty', models.DecimalField(decimal_places=2, default=1, max_digits=17, verbose_name='Ποσότητα')),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Εκπτωση')),
                ('discount_value', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Ποσο Εκπτωσης')),
                ('clean_value', models.DecimalField(decimal_places=2, default=0, max_digits=17, verbose_name='Καθαρη Αξια')),
                ('total_clean_value', models.DecimalField(decimal_places=2, max_digits=17, verbose_name='Συνολική Καθαρη Αξια')),
                ('taxes_modifier', models.CharField(choices=[('a', 0), ('d', 6), ('b', 13), ('c', 24)], default='c', max_length=1, verbose_name='ΦΠΑ')),
                ('taxes_value', models.DecimalField(decimal_places=2, max_digits=17, verbose_name='Αξια ΦΠΑ')),
                ('total_value', models.DecimalField(decimal_places=2, max_digits=17, verbose_name='Τελικη Αξία')),
                ('sell_price', models.DecimalField(decimal_places=2, default=0, max_digits=17, verbose_name='Tιμη Πωλησης')),
                ('invoice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_items', to='costumers.paymentinvoice')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
