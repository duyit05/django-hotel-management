from django.db import models

class RoomType(models.TextChoices):
    STANDARD = '0', 'Standard'
    BASIC = '1', 'Basic'
    DELUXE = '2', 'Deluxe'