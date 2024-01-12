from django.shortcuts import get_object_or_404, HttpResponseRedirect
from django.template.loader import render_to_string

from functools import reduce
from django.db.models import Q
from operator import or_

from django.http import JsonResponse
from django.contrib.admin.views.decorators import staff_member_required


from .models import PriceList, Product, PriceListItem
from .forms import ProductListItemForm


@staff_member_required
def ajax_add_product_to_price_list_view(request, pk, dk, action):
    product = get_object_or_404(Product, id=dk)
    price_list = get_object_or_404(PriceList, id=pk)
    instance = PriceListItem.objects.create(
        product=product,
        price_list=price_list,
        qty=1,
        value=product.value
    )

    data = dict()
    qs = PriceListItem.objects.filter(price_list=price_list)
    data["result"] = render_to_string(
        template_name="products/ajax_price_list_products.html",
        request=request,
        context={
            "qs": qs,
            "object": price_list
        }
    )
    
    return JsonResponse(data)


def ajax_search_products(request, pk):
    data = dict()
    price_list = get_object_or_404(PriceList, id=pk)
    search_name = request.GET.get('search_name', None)
    qs = Product.objects.none()
    if len(search_name):
        qs = Product.objects.filter(title__icontains=search_name)
    data['result'] = render_to_string(template_name='products/ajax_products_search.html', request=request, context={'products': qs, "object": price_list})
    return JsonResponse(data)



@staff_member_required
def ajax_edit_product_submit_view(request, pk, dk):
    # deprecicated
    data = dict()
    price_list = get_object_or_404(PriceList, id=pk)
    instance = get_object_or_404(PriceListItem, id=dk)
    form = ProductListItemForm(request.POST or None, instance=instance,
                                initial={
                                    "product": instance.product,
                                    "price_list": instance.price_list}
                                    )
    pr
    if form.is_valid():
        form.save()
    else:
        print(form.errors)
    return HttpResponseRedirect(price_list.get_absolute_url())


@staff_member_required
def create_product_from_price_time_view(request, pk):
    price_list = get_object_or_404(PriceList, id=pk)
    form = ProductListItemForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        instance.price_list.add(price_list)
        instance.save()

    return HttpResponseRedirect(price_list.get_absolute_url())



@staff_member_required
def ajax_delete_price_item_view(request, pk):
    price_item = get_object_or_404(PriceListItem, id=pk)
    price_list = price_item.price_list
    price_item.delete()
    data = dict()
    qs = PriceListItem.objects.filter(price_list=price_list)
    data["result"] = render_to_string(
        template_name="products/ajax_price_list_products.html",
        request=request,
        context={
            "qs": qs,
            "object": price_list
        }
    )
    
    return JsonResponse(data)