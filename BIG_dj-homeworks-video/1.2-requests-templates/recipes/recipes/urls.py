from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from calculator.views import dish_show, dish_show_total, index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('<name>/<servings>', dish_show_total),
    path('<name>/', dish_show),
    path('', index),
]
