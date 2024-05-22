from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Slot, Booking
from .forms import BookingForm

def available_slots(request):
    today = timezone.now().date()
    slots = Slot.objects.filter(date__gte=today, slots_available__gt=0).order_by('date')
    return render(request, 'booking/available_slots.html', {'slots': slots})

def book_slot(request, slot_id):
    slot = get_object_or_404(Slot, id=slot_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.slot = slot
            booking.save()
            slot.slots_available -= 1
            slot.save()
            return redirect('available_slots')
    else:
        form = BookingForm()
    return render(request, 'booking/book_slot.html', {'form': form, 'slot': slot})
