from django.contrib import admin
from .models import Room, Booking

# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'capacity')
    search_fields = ('name')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'start_time', 'end_time', 'status')
    list_filter = ('status', 'room')
    search_fields = ('user_name', 'room_name')
