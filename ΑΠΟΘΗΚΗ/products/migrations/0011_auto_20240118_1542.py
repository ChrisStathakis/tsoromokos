# Generated by Django 3.2.7 on 2024-01-18 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20240118_1332'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='categorypricelist',
            options={'ordering': ['category__title', 'title']},
        ),
        migrations.AlterField(
            model_name='pricelistitem',
            name='discount_percent',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='ΕΚΠΤΩΣΗ ΠΟΣΟΣΤΟ'),
        ),
        migrations.AlterField(
            model_name='pricelistitem',
            name='final_value_margin',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='ΑΞΙΑ ΠΩΛΗΣΗΣ'),
        ),
        migrations.AlterField(
            model_name='pricelistitem',
            name='final_value_unit',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='ΤΕΛΙΚΗ ΤΙΜΗ ΜΟΝΑΔΑΣ'),
        ),
    ]
