from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from books.models import Book

def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    return render(request, template, {'books': books})

def sort_name(request):
    template = 'books/books_list.html'
    books = Book.objects.filter().order_by('name')
    return render(request, template, {'books' : books})

def sort_date_old(request):
    template = 'books/books_list.html'
    books = Book.objects.filter().order_by('pub_date')
    return render(request, template, {'books' : books})

def sort_date_new(request):
    template = 'books/books_list.html'
    books = Book.objects.filter().order_by('pub_date').reverse()
    return render(request, template, {'books' : books})



def books_date(request, date):
    template = 'books/books_list.html'

    # достаем конкретные данные через value_list. а именно список со всеми датами.
    list_time_date = list(Book.objects.values_list('pub_date', flat=True).order_by('pub_date'))
    print(list_time_date)

    #достаем индекс в списке
    date_index = list_time_date.index(date)
    # теперь по индексу-дате достаем уже все данные по книге
    context = {'books': Book.objects.filter(pub_date=date)}

    # делаем
    context['prev_page'] = (
        list_time_date[date_index-1] if date_index != 0 else None
    )
    context['next_page'] = (
        list_time_date[date_index+1] if date_index != (len(list_time_date)-1) else None
    )

    return render(request, template, context)