from django.db import  models
class RoomStatus (models.TextChoices):
    AVAILABLE = '0','Available'
    BOOKED = '1','Booked'
    MAINTENANCE = '2','Maintenance'