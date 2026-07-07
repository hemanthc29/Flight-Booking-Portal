from django.test import TestCase
from django.utils import timezone
from datetime import datetime, timedelta
from django.contrib.auth import get_user_model

from flights.models import Airline, Airport, Aircraft, Route, Flight, Seat, Review

User = get_user_model()

class FlightModelTests(TestCase):
    def setUp(self):
        self.airline = Airline.objects.create(
            name="Test Airways",
            code="TA"
        )
        self.origin = Airport.objects.create(
            name="Origin Field",
            code="ORF",
            city="New York",
            country="USA"
        )
        self.destination = Airport.objects.create(
            name="Destination Port",
            code="DTP",
            city="London",
            country="UK"
        )
        self.route = Route.objects.create(
            origin=self.origin,
            destination=self.destination,
            distance=5500.0,
            duration=timedelta(hours=7)
        )
        self.aircraft = Aircraft.objects.create(
            model_name="777",
            manufacturer="Boeing",
            capacity=100
        )
        
        self.departure = timezone.now() + timedelta(days=1)
        self.arrival = self.departure + timedelta(hours=7)
        
        self.flight = Flight.objects.create(
            flight_number="TA101",
            airline=self.airline,
            aircraft=self.aircraft,
            route=self.route,
            departure_time=self.departure,
            arrival_time=self.arrival,
            base_fare=350.00
        )

    def test_flight_duration(self):
        """Verify the flight duration property matches departure/arrival difference."""
        self.assertEqual(self.flight.duration, timedelta(hours=7))

    def test_seat_generation(self):
        """Verify adding seats to flights works as expected."""
        seat = Seat.objects.create(
            flight=self.flight,
            seat_number="1A",
            seat_class="First",
            seat_type="Window",
            price_multiplier=1.80
        )
        self.assertEqual(seat.seat_number, "1A")
        self.assertFalse(seat.is_reserved)
        self.assertEqual(self.flight.seats.count(), 1)
