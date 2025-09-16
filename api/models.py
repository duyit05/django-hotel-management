from django.db import models

from api.enums.room_status import RoomStatus
from api.enums.room_type import RoomType


# Create your models here.
class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_number = models.IntegerField()
    room_type = models.CharField(max_length=1, choices=RoomType.choices, default=RoomType.STANDARD)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField()
    status = models.CharField(max_length=1, choices=RoomStatus.choices, default=RoomStatus.AVAILABLE)
    description = models.TextField()
    floor = models.IntegerField()
    images = models.ImageField(upload_to='rooms/', blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
