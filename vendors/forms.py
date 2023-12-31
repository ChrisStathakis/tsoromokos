
from django import forms
from tinymce.widgets import TinyMCE

from .models import (Vendor, Invoice, Payment, Vendor, Employer,
                    VendorBankingAccount, Note, TAXES_CHOICES,
                    Paycheck, InvoiceItem
                    
                    )

from products.models import Product, ProductVendor


class BaseForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class VendorForm(BaseForm, forms.ModelForm):
    site = forms.URLField(widget=forms.TextInput(), required=False)

    class Meta:
        model = Vendor
        fields = ['active', 'title', 'job_description','identifier','owner', 'afm', 'doy', 'phone', 'cellphone', 'address', 'email', 'site', 'taxes_modifier']

    def clean_site(self):
        data = self.cleaned_data.get('site', None)
        if data:
            if not 'http' in data:
                data = 'https://'+ data
        return data


class InvoiceVendorDetailForm(BaseForm, forms.ModelForm):
    vendor = forms.ModelChoiceField(queryset=Vendor.objects.all(), widget=forms.HiddenInput())
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True, label='Ημερομηνία')

    class Meta:
        model = Invoice
        fields = ['date', 'title', 'vendor', 'value', 'extra_value', 'payment_method', 'description', 'taxes_6', 'taxes_13', 'taxes_24']


class InvoiceForm(BaseForm, forms.ModelForm):
    vendor = forms.ModelChoiceField(queryset=Vendor.objects.all(), widget=forms.HiddenInput())
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True, label='Ημερομηνία')

    class Meta:
        model = Invoice
        fields = ['date', 'vendor', 'title', 'payment_method', 'description', 'extra_value']


class PaymentForm(BaseForm, forms.ModelForm):
    vendor = forms.ModelChoiceField(queryset=Vendor.objects.all(), widget=forms.HiddenInput())
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True)
    
    class Meta:
        model = Payment
        fields = '__all__'


class EmployerForm(BaseForm, forms.ModelForm):
    vendor = forms.ModelChoiceField(queryset=Vendor.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = Employer
        fields = '__all__'


class VendorBankingAccountForm(BaseForm, forms.ModelForm):
    vendor = forms.ModelChoiceField(queryset=Vendor.objects.all(), widget=forms.HiddenInput())
    
    class Meta:
        model = VendorBankingAccount
        fields = '__all__'


class NoteForm(BaseForm, forms.ModelForm):
    vendor_related = forms.ModelChoiceField(queryset=Vendor.objects.all(), widget=forms.HiddenInput())
    text = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 200}))
    
    class Meta:
        model = Note
        fields = ['status', 'title', 'text', 'vendor_related']


class VendorProductForm(BaseForm, forms.ModelForm):
    warehouse_value = forms.DecimalField(required=True, label='Αξια Τιμολογιου')
    discount = forms.IntegerField(required=True, label='Εκπτωση Τιμολογιου')
    extra_value = forms.DecimalField(required=True, label='Επιπλεον Αξια')
    taxes_modifier = forms.ChoiceField(choices=TAXES_CHOICES, label='ΦΠΑ')
    is_favorite = forms.BooleanField(label='Αγαπημένο', required=False)
    sku_ware = forms.CharField(label='Κωδικός Τιμολογίου', required=False)
    
    class Meta:
        model = Product
        fields = ['active', 'is_favorite', 'title', 'sku', 'categories',
                  'sku_ware',
                  'warehouse_value', 'discount', 'extra_value',  
                  'qty', 'value', 'taxes_modifier', 
                  
        ]


class ProductVendorClassForm(BaseForm, forms.ModelForm):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), widget=forms.HiddenInput())
    vendor = forms.ModelChoiceField(queryset=Vendor.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = ProductVendor
        fields = ['is_favorite', 'product', 'vendor', 'sku', 'value',
                  'discount', 'added_value', 'taxes_modifier'
        ]
        

class CopyProductToNewVendor(BaseForm):
    vendor = forms.ModelChoiceField(queryset=Vendor.objects.all(), label='Προμηθευτής')
    value = forms.DecimalField(required=True)
    discount = forms.IntegerField(required=True)
    added_value = forms.DecimalField(required=True)


class CopyProductFromVendorCardForm(BaseForm, forms.ModelForm):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), widget=forms.HiddenInput())
    vendor = forms.ModelChoiceField(queryset=Vendor.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = ProductVendor
        fields = ['product', 'vendor', 'sku', 'value', 'discount', 'added_value','taxes_modifier']

    
class PaycheckForm(BaseForm, forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True)

    class Meta:
        model = Paycheck
        fields = ['is_done', 'date', 'vendor', 'title', 'value']


class InvoiceProductForm(BaseForm, forms.ModelForm):
    vendor = forms.ModelChoiceField(queryset=Vendor.objects.all(), widget=forms.HiddenInput(), required=True)
    qty = forms.DecimalField(label='Ποσότητα', required=True)
    price_buy = forms.DecimalField(label='Αξια', widget=forms.NumberInput(attrs={'step': '0.001'}))

    class Meta:
        model = Product
        fields = ['order_code', 'title', 'taxes_modifier',
                  'unit',
                  'vendor', 'price_buy',
                  'qty', 'value'
                ]


class InvoiceItemForm(BaseForm, forms.ModelForm):
    vendor = forms.ModelChoiceField(queryset=Vendor.objects.all(), widget=forms.HiddenInput())
    invoice = forms.ModelChoiceField(queryset=Invoice.objects.all(), widget=forms.HiddenInput())
    product = forms.ModelChoiceField(queryset=Product.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = InvoiceItem
        fields = ['order_code', 'unit', 'qty', 'value', 'discount',
                  'taxes_modifier', 'vendor', 'invoice', 'product'
                  ]
