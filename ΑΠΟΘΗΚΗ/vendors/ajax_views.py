from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Sum
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, reverse
from django.utils import timezone

from .forms import InvoiceForm, InvoiceItemForm
from .models import Invoice, Payment, Vendor, Employer, VendorBankingAccount, Note, InvoiceItem
from products.models import Product, ProductVendor, Category
from products.forms import ProductClassForm, ProductFrontEndForm

from frontend.models import Settings
from .forms import (InvoiceForm, EmployerForm, VendorBankingAccountForm,
                    PaymentForm, NoteForm, VendorProductForm, ProductVendorClassForm,
                    Invoice, InvoiceForm
                    )
from .tables import ProductVendorTable


from products.tables import ProductTableForCategory


from django_tables2 import RequestConfig



def ajax_invoice_modal_view(request, pk):
    invoice = get_object_or_404(Invoice, id=pk)
    form = InvoiceForm(instance=invoice)
    form_title, valid_url = f'Επεξεργασια Παραστατικού { invoice }', reverse('vendors:validate_invoice_edit_view', kwargs={'pk': invoice.id})
    delete_url = reverse('vendors:action_delete_invoice', kwargs={'pk': invoice.id})
    data = dict()
    data['result'] = render_to_string(request=request,
                                      template_name='vendors/ajax_views/modal_form.html',
                                      context=locals(),
                                      )
    return JsonResponse(data)


def ajax_payment_edit_modal_view(request, pk):
    payment = get_object_or_404(Payment, id=pk)
    form = PaymentForm(instance=payment)
    form_title, valid_url = f'Επεξεργασια πληρωμής { payment }', reverse('vendors:validate_payment_edit_view', kwargs={'pk': payment.id})
    delete_url = reverse('vendors:action_delete_payment', kwargs={'pk': payment.id})
    data = dict()
    data['result'] = render_to_string(request=request,
                                      template_name='vendors/ajax_views/modal_form.html',
                                      context=locals(),
                                      )
    return JsonResponse(data)

def ajax_employer_edit_modal_view(request, pk):
    employer = get_object_or_404(Employer, id=pk)
    form = EmployerForm(instance=employer)
    form_title, valid_url = f'Επεξεργασία {employer.title}', reverse('vendors:validate_employer_edit_view', kwargs={'pk': employer.id})
    delete_url = reverse('vendors:action_delete_employer', kwargs={'pk': employer.id})
    data = dict()
    data['result'] = render_to_string(request=request,
                                      template_name='vendors/ajax_views/modal_form.html',
                                      context=locals(),
                                      )
    return JsonResponse(data)


def ajax_banking_account_edit_modal_view(request, pk):
    banking_account = get_object_or_404(VendorBankingAccount, id=pk)
    form = EmployerForm(instance=banking_account)
    form_title, valid_url = f'Επεξεργασία {banking_account}', reverse('vendors:validate_employer_edit_view', kwargs={'pk': banking_account.id})
    delete_url = reverse('vendors:delete_account_banking_view', kwargs={'pk': banking_account.id})
    data = dict()
    data['result'] = render_to_string(request=request,
                                      template_name='vendors/ajax_views/modal_form.html',
                                      context=locals(),
                                      )
    return JsonResponse(data)


def ajax_banking_account_create_modal_view(request, pk):
    vendor = get_object_or_404(Vendor, id=pk)
    form = VendorBankingAccountForm(initial={'vendor': vendor})
    form_title, valid_url = f'Δημιουργία', reverse('vendors:validate_create_banking_account', kwargs={'pk': vendor.id})
    data = dict()
    data['result'] = render_to_string(request=request,
                                      template_name='vendors/ajax_views/modal_form.html',
                                      context=locals(),
                                      )
    return JsonResponse(data)


def ajax_banking_account_edit_modal_view(request, pk):
    banking_account = get_object_or_404(VendorBankingAccount, id=pk)
    form = VendorBankingAccountForm(instance=banking_account)
    form_title, valid_url = f'Επεξεργασια', reverse('vendors:validate_edit_banking_account', kwargs={'pk': banking_account.id})
    delete_url = reverse('vendors:delete_account_banking_view', kwargs={'pk': banking_account.id})
    data = dict()
    data['result'] = render_to_string(request=request,
                                      template_name='vendors/ajax_views/modal_form.html',
                                      context=locals(),
                                      )
    return JsonResponse(data)


@staff_member_required
def ajax_show_product_prices(request, pk):
    instance = get_object_or_404(Product, id=pk)
    order_items = instance.invoice_vendor_items.all()[:10]
    data = dict()
    data['result'] = render_to_string(request=request,
                                      template_name='vendors/ajax_views/modal_product_price.html',
                                      context={
                                          'product': instance,
                                          'order_items': order_items,
                                      }
                                      )
    return JsonResponse(data)


@staff_member_required
def ajax_show_product_analysis_view(request, pk):
    instance = get_object_or_404(Product, id=pk)
    data = dict()
    data['result'] = render_to_string(request=request,
                                      template_name='vendors/ajax_views/modal_product_analysis.html',
                                      context={
                                          'instance': instance
                                      }
                                      )
    return JsonResponse(data)


@staff_member_required
def ajax_search_warehouse_view(request, pk):
    vendor = get_object_or_404(Vendor, id=pk)
    print('dada')
    
    qs = Product.filters_data(request, Product.objects.filter(active=True))[:20]
    
    data = dict()
    data['result'] = render_to_string(template_name='vendors/ajax_views/ajax_product_container.html',
                                      request=request,
                                      context={
                                          'queryset_table': ProductVendorTable(qs),
                                          'vendor': vendor
                                      }
                                      )
    return JsonResponse(data)


@staff_member_required 
def ajax_calculate_vendors_balance_view(request):
    vendors = Vendor.filters_data(request, Vendor.objects.all())
    total_balance = vendors.aggregate(Sum('balance'))['balance__sum'] if vendors else 0
    data = dict()
    data['result'] = render_to_string(request=request,
                                      template_name='ajax_views/calculate_balance_view.html',
                                      context = {
                                          'total_balance':total_balance
                                      }
                                      )
    return JsonResponse(data)


@staff_member_required
def ajax_edit_product_modal(request, pk):
    instance = get_object_or_404(ProductVendor, id=pk)
    product = instance.product
    product = get_object_or_404(Product, id=product.id)
    form = ProductVendorClassForm(request.POST or None ,instance=instance)
    product_form = ProductClassForm(instance=product)
    data = dict()
    data['result'] = render_to_string(template_name='vendors/ajax_views/modal_form.html',
                                      request=request,
                                      context={
                                          'form': form,
                                          'title': f'Επεξεργασία {instance}',
                                          'product_form': product_form,
                                          'product': product,
                                          'valid_url': reverse('vendors:validate_product_vendor_edit', kwargs={'pk': instance.id}),
                                          'product_valid_url': reverse('vendors:validate_product_edit', kwargs={'pk': product.id}),
                                          'instance': instance
                                          
                                      }
                                    )
    return JsonResponse(data)


@staff_member_required
def ajax_product_modal_quick_view(request, pk):
    instance = get_object_or_404(Product, id=pk)
    data = dict()
    data['result'] = render_to_string(template_name='vendors/ajax_views/ajax_product_modal_quick_view.html',
                                      request=request,
                                      context={
                                          'instance': instance
                                      }
                                      )
    return JsonResponse(data)


# category ajax calls
@staff_member_required
def ajax_add_product_to_category_view(request, pk, dk, action):
    print("data", dk, pk, action)
    product = get_object_or_404(Product, id=dk)
    category = get_object_or_404(Category, id=pk)
    product.categories.add(category) if action == 'add' else product.categories.remove(category)
    product.save()
    data = dict()
    qs = Product.objects.filter(categories=category)
    data["result"] = render_to_string(
        template_name="categories/ajax/ajax_category_products.html",
        request=request,
        context={
            "category": category,
            "qs":  qs
        }
    )

    return JsonResponse(data)


def ajax_search_products(request, pk):
    data = dict()
    category = get_object_or_404(Category, id=pk)
    search_name = request.GET.get('search_name', None)
    qs = Product.objects.none()
    if len(search_name):
        qs = Product.objects.filter(title__icontains=search_name)
    data['result'] = render_to_string(template_name='categories/ajax/ajax_products_search.html', request=request,
                                      context={'products': qs, "category": category})
    return JsonResponse(data)


@staff_member_required
def ajax_edit_product_submit_view(request, pk, dk):
    category = get_object_or_404(Category, id=pk)
    instance = get_object_or_404(Product, id=dk)
    form = ProductFrontEndForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
    return HttpResponseRedirect(category.get_card_url())


@staff_member_required
def create_product_from_category_view(request, pk):
    category = get_object_or_404(Category, id=pk)
    form = ProductFrontEndForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        instance.categories.add(category)
        instance.save()
    return HttpResponseRedirect(category.get_card_url())



@staff_member_required
def ajax_search_products_warehouse_view(request, pk):
    instance = get_object_or_404(Invoice, id=pk)
    products = Product.filters_data(request, Product.objects.all())
    data = dict()
    data['result'] = render_to_string(template_name='warehouse/ajax/ware_product_container.html',
                                      request=request,
                                      context={
                                          'products': products,
                                          'object': instance,
                                      }
                                    )
    return JsonResponse(data)



@staff_member_required
@csrf_exempt
def ajax_modify_order_item_modal(request, pk):
    instance = get_object_or_404(InvoiceItem, id=pk)
    form = InvoiceItemForm(instance=instance, initial={'income_percent': Settings.objects.first().income_percent or 0})
    data = dict()
    
    data['result'] = render_to_string(template_name='warehouse/ajax/product_modal.html',
                                      request=request,
                                      context={
                                          'form': form,
                                          'title': f'Επεξεργασια {instance.product}',
                                          'action_url': reverse('vendors:validate_order_item_update', kwargs={'pk': instance.id}),
                                          'delete_url': instance.get_delete_url()

                                      }
                                      )
    return JsonResponse(data)


@staff_member_required
@staff_member_required
def ajax_create_product_modal(request, pk, dk):
    invoice = get_object_or_404(Invoice, id=pk)
    product = get_object_or_404(Product, id=dk)
    data = dict()
    action_url = reverse("vendors:validate_order_item_creation", kwargs={'pk': invoice.id})
    form = InvoiceItemForm(initial={
                                    'vendor': invoice.vendor,
                                    'invoice': invoice,
                                    'product': product,
                                    'taxes_modifier': product.taxes_modifier,
                                    'value': product.price_buy,
                                    'income_percent': Settings.objects.first().income_percent if Settings.objects.all().exists() else 0
                                    }
                           )
    data['result'] = render_to_string(request=request,
                                      template_name='warehouse/ajax/product_modal.html',
                                      context={
                                          'form': form,
                                          'product': product,
                                          'action_url': action_url,
                                          'invoice': invoice,
                                          'title': product
                                          }
                                    )
    return JsonResponse(data)


@staff_member_required
def ajax_search_products_invoice(request):
    products = Product.filters_data(request=request, qs=Product.objects.filter(active=True))
