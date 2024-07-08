from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100)  # Назва кімнати
    description = models.TextField()  # Опис кімнати
    price = models.IntegerField()  # Ціна
    capacity = models.IntegerField()  # Вмістимість в кімнаті
    features = models.TextField()  # Особливості

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Користувач
    room = models.ForeignKey(Room, on_delete=models.CASCADE)  # Кімната
    start_time = models.DateTimeField()  # Початок
    end_time = models.DateTimeField()  # Кінець
    creation_time = models.DateTimeField(auto_now_add=True)  # Час створення бронювання
    status = models.CharField(max_length=100, default='pending')  # Статус бронювання

    def __str__(self):
        return f'Booking by {self.user.name} for {self.room.name}'

    class Meta:
        unique_together = (('room', 'start_time', 'end_time'),)
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
        ordering = ['start_time']