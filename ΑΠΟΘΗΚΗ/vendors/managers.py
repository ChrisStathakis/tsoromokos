from django.db import models



class InvoiceItemManager(models.Manager):

    def return_products(self, q):
        ids = self.filter(order_code__icontains=q).distinct().values_list('product__id')
        return ids

