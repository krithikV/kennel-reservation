from django.contrib import admin
from .models import Slot, Booking

def create_week_slots(modeladmin, request, queryset):
    from django.utils import timezone
    from datetime import timedelta

    today = timezone.now().date()
    for day in range(7):
        date = today + timedelta(days=day)
        Slot.objects.get_or_create(date=date, defaults={'slots_available': 30})
    modeladmin.message_user(request, "Slots for the upcoming week have been created.")

create_week_slots.short_description = 'Create slots for the upcoming week'

class SlotAdmin(admin.ModelAdmin):
    list_display = ('date', 'slots_available')
    actions = [create_week_slots]

class BookingAdmin(admin.ModelAdmin):
    list_display = ('slot', 'owner_name', 'pet_name', 'contact_number')

admin.site.register(Slot, SlotAdmin)
admin.site.register(Booking, BookingAdmin)
