# Generated by Django 3.2.7 on 2023-11-27 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralExpenseCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='Ονομασια')),
            ],
        ),
        migrations.CreateModel(
            name='GeneralExpense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, verbose_name='Περιγραφη')),
                ('value', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Αξια')),
                ('paid_value', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Πληρωτεο Ποσο')),
                ('is_paid', models.BooleanField(default=True, verbose_name='Πληρωμενο;')),
                ('date', models.DateField(verbose_name='Ημερομηνια')),
                ('taxes_6', models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='ΠΟΣΟ ΦΠΑ 6%')),
                ('taxes_13', models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='ΠΟΣΟ ΦΠΑ 13%')),
                ('taxes_24', models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='ΠΟΣΟ ΦΠΑ 24%')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='general_expenses.generalexpensecategory', verbose_name='Κατηγορια')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]