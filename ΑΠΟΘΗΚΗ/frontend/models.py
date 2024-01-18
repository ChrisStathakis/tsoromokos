from django.db import models

# Create your models here.

PAYMENT_METHOD_CATEGORY = (
    ('a', 'Αντικαταβολή'),
    ('b', 'Τραπεζική ΚατάΘεση')
)


class PaymentMethod(models.Model):
    title = models.CharField(max_length=200, unique=True)
    category = models.CharField(max_length=1, choices=PAYMENT_METHOD_CATEGORY)

    def __str__(self):
        return self.title


class Settings(models.Model):
    income_percent = models.DecimalField(default=20, decimal_places=2, max_digits=5)
    initial_years_filter = models.PositiveIntegerField(default=2)


    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return 'Settings'