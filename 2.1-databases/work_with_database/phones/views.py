from django.shortcuts import render, redirect
from django.http import HttpResponse
from phones.models import Phone


def index(request):
    return redirect('catalog')

def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()

    sort_dict = {
        'name': 'name',
        'min_price': 'price',
        'max_price': '-price'
    }
    sort = request.GET.get('sort')

    if sort:
        phones = phones.order_by(sort_dict.get(sort))
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug).first()
    context = {'phone': phone}
    return render(request, template, context)