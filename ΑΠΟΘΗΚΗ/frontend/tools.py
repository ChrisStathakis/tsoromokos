from urllib.parse import urlencode
from django.shortcuts import reverse

import datetime
from dateutil.relativedelta import relativedelta

from .models import Settings
from decimal import Decimal

def remove_exponent(d):
    return (
        d.quantize(Decimal(1))
        if d == d.to_integral()
        else d.normalize()
    )

def build_url(*args, **kwargs):
    get = kwargs.pop('get', {})
    url = reverse(*args, **kwargs)
    if get:
        url += '?' + urlencode(get)
    return url


def initial_date(request, months=12):
    settings = Settings.objects.first()
    #  gets the initial last three months or the session date
    # months will get deprecicated
    date_now = datetime.datetime.today()
    if settings:
        current_year = f'01/01/{(datetime.date.today()- relativedelta(year=settings.initial_years_filter)).year} - 12/31/{datetime.date.today().year}'
    else: 
        current_year = f'01/01/{(datetime.date.today()- relativedelta(year=2)).year} - 12/31/{datetime.date.today().year}'
    current_year = f'01/01/{(datetime.date.today() - relativedelta(year=2)).year} - 12/31/{datetime.date.today().year}'
    print(current_year)
    date_range = request.GET.get('date_range', current_year)
    date_start, date_end = None, None

    if date_range:
        try:
            date_range = date_range.split('-')
            date_range[0] = date_range[0].replace(' ','')
            date_range[1] = date_range[1].replace(' ','')
            date_start = datetime.datetime.strptime(date_range[0], '%m/%d/%Y')
            date_end = datetime.datetime.strptime(date_range[1],'%m/%d/%Y')
        except:
            print('except hitted')
            date_three_months_ago = date_now - relativedelta(months=months)
            date_start = date_three_months_ago
            date_end = date_now
            date_range = '%s - %s' % (str(date_three_months_ago).split(' ')[0].replace('-','/'),str(date_now).split(' ')[0].replace('-','/'))
            request.session['date_range'] = '%s - %s'%(str(date_three_months_ago).split(' ')[0].replace('-','/'),str(date_now).split(' ')[0].replace('-','/'))
    return [date_start, date_end, date_range]
