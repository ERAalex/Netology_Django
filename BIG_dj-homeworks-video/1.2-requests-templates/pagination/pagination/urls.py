

from django.urls import path, include

urlpatterns = [
    path('', include('stations.urls')),
]
