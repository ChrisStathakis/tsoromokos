from django.dispatch import receiver
from django.db.models.signals import post_delete

from .models import PriceListItem

@receiver(post_delete, sender=PriceListItem)
def update_price_list_after_delete(sender, instance, **kwargs):
    instance.price_list.save()