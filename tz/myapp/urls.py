from django.urls import path
from .views import *

urlpatterns = [
    path('booking_form', book_room, name='booking_form'),
]