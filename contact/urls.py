from django.urls import path

from contact.views import index

urlpatterns = [
    path('', index, name='index'),
]
