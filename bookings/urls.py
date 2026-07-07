from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('book/<int:flight_id>/', views.book_flight_view, name='book_flight'),
    path('my-bookings/', views.my_bookings_view, name='my_bookings'),
    path('cancel/<int:booking_id>/', views.cancel_booking_view, name='cancel_booking'),
    path('ticket/<int:ticket_id>/download/', views.download_ticket_view, name='download_ticket'),
]
