from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open('data-398-2018-08-30.csv', newline='', encoding='utf-8' ) as csvfile:
        csv_file = list(csv.DictReader(csvfile))

    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(csv_file, 10)
    stations = paginator.get_page(page_number)
    context = {
        'bus_stations': stations,
        'page': stations
    }
    return render(request, 'stations/index.html', context)
