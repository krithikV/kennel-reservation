from django.urls import path
from . import views

urlpatterns = [
    path('', views.available_slots, name='available_slots'),
    path('book/<int:slot_id>/', views.book_slot, name='book_slot'),
]
