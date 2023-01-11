from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):

    sort_block = request.GET.get('sort', 'name')

    if sort_block == 'name':
        phones = Phone.objects.order_by('name')
    elif sort_block == 'min_price':
        phones = Phone.objects.order_by('price')
    elif sort_block == 'max_price':
        phones = Phone.objects.order_by('-price')
    else:
        phones = Phone.objects.all()
    template = 'catalog.html'
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
