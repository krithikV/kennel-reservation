from django.db import models
from django.utils import timezone
from datetime import timedelta

class Slot(models.Model):
    date = models.DateField(unique=True)
    slots_available = models.IntegerField(default=30)

    def __str__(self):
        return f"{self.date} ({self.slots_available} slots available)"

    @classmethod
    def create_week_slots(cls):
        today = timezone.now().date()
        for day in range(7):
            date = today + timedelta(days=day)
            cls.objects.get_or_create(date=date, defaults={'slots_available': 30})

class Booking(models.Model):
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)
    owner_name = models.CharField(max_length=100)
    pet_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.owner_name} - {self.pet_name} ({self.slot.date})"
