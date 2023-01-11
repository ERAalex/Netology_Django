from django.contrib import admin
from django.urls import path, register_converter
from books.converters import PubDateConverter

from books.views import books_view, books_date, sort_name, sort_date_new, sort_date_old

register_converter(PubDateConverter, 'pub_date')

urlpatterns = [
    path('', books_view, name='books'),
    path('books/<pub_date:date>/', books_date, name='date'),

    path('admin/', admin.site.urls),
    path('books_name', sort_name, name='sort_name'),
    path('books_old', sort_date_new, name='sort_date_old'),
    path('books_new', sort_date_old, name='sort_date_new'),



]
