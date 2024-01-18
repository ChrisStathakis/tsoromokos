# Generated by Django 3.2.7 on 2024-01-16 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0004_auto_20240116_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='extra_value',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='ΜΕΤΑΦΟΡΙΚΑ'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='final_value',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='Αξία'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Καθαρή Αξια'),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='discount_value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Ποσο Εκπτωσης'),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=17, verbose_name='Τιμή Μοναδας'),
        ),
    ]
