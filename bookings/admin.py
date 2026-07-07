from django.contrib import admin
from .models import Booking, Passenger, Wishlist

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('pnr', 'user', 'flight', 'booking_date', 'status', 'total_amount')
    list_filter = ('status',)
    search_fields = ('pnr', 'user__username', 'flight__flight_number')

@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'booking', 'seat')

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'flight', 'created_at')
