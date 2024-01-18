from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from frontend.models import PaymentMethod, PAYMENT_METHOD_CATEGORY, Settings


@admin.register(PaymentMethod)
class PaymentMethodAdmin(ImportExportModelAdmin):
    pass


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    pass



