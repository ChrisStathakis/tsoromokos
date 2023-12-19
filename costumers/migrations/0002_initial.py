# Generated by Django 3.2.7 on 2023-12-19 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('costumers', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoiceitem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sell_items', to='products.product', verbose_name='Προϊον'),
        ),
        migrations.AddField(
            model_name='costumerdetails',
            name='costumer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='costumers.costumer'),
        ),
        migrations.AddField(
            model_name='costumerdetails',
            name='invoice',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='profile', to='costumers.paymentinvoice'),
        ),
        migrations.AlterUniqueTogether(
            name='paymentinvoice',
            unique_together={('number', 'series', 'order_type')},
        ),
    ]
