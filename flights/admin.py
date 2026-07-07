from django.contrib import admin
from .models import Airline, Airport, Aircraft, Route, Flight, Seat, Review, ContactMessage, NewsletterSubscriber

@admin.register(Airline)
class AirlineAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'contact_details')

@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'city', 'country')
    search_fields = ('name', 'code', 'city')

@admin.register(Aircraft)
class AircraftAdmin(admin.ModelAdmin):
    list_display = ('model_name', 'manufacturer', 'capacity')

@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('origin', 'destination', 'distance', 'duration')

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('flight_number', 'airline', 'departure_time', 'arrival_time', 'base_fare', 'status')
    list_filter = ('status', 'airline', 'cabin_class')
    search_fields = ('flight_number',)

@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ('flight', 'seat_number', 'seat_class', 'seat_type', 'is_reserved')
    list_filter = ('seat_class', 'seat_type', 'is_reserved')
    search_fields = ('seat_number', 'flight__flight_number')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'flight', 'rating', 'travel_date')
    list_filter = ('rating',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')

@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')
