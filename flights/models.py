from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

class Airline(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    logo = models.ImageField(upload_to='airline_logos/', blank=True, null=True)
    contact_details = models.TextField(blank=True, null=True)
    fleet_details = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Airport(models.Model):
    code = models.CharField(max_length=10, unique=True) # IATA code (e.g. JFK)
    name = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    terminal_info = models.TextField(blank=True, null=True)
    contact_details = models.TextField(blank=True, null=True)
    map_embed_url = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.code})"

class Aircraft(models.Model):
    model_name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.manufacturer} {self.model_name}"

class Route(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='route_origins')
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='route_destinations')
    distance = models.DecimalField(max_digits=8, decimal_places=2, help_text="in km")
    duration = models.DurationField(help_text="Expected duration of flight")

    def __str__(self):
        return f"{self.origin.code} to {self.destination.code}"

class Flight(models.Model):
    STATUS_CHOICES = (
        ('Scheduled', 'Scheduled'),
        ('Delayed', 'Delayed'),
        ('Cancelled', 'Cancelled'),
        ('Completed', 'Completed'),
    )
    
    CABIN_CHOICES = (
        ('Economy', 'Economy'),
        ('Business', 'Business'),
        ('First', 'First'),
    )

    flight_number = models.CharField(max_length=20, unique=True)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE, related_name='flights')
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    base_fare = models.DecimalField(max_digits=10, decimal_places=2)
    cabin_class = models.CharField(max_length=20, choices=CABIN_CHOICES, default='Economy')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Scheduled')
    baggage_allowance = models.CharField(max_length=100, default='15kg check-in, 7kg cabin')
    refund_policy = models.TextField(default='Refundable with deduction fee. Cancel before 24 hours.')
    meals_included = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.flight_number} - {self.route}"

    @property
    def duration(self):
        return self.arrival_time - self.departure_time

class Seat(models.Model):
    SEAT_CLASS_CHOICES = (
        ('Economy', 'Economy'),
        ('Business', 'Business'),
        ('First', 'First'),
    )
    SEAT_TYPE_CHOICES = (
        ('Window', 'Window'),
        ('Aisle', 'Aisle'),
        ('Middle', 'Middle'),
        ('Emergency Exit', 'Emergency Exit'),
    )

    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='seats')
    seat_number = models.CharField(max_length=10) # e.g. 12A, 1B
    seat_class = models.CharField(max_length=20, choices=SEAT_CLASS_CHOICES, default='Economy')
    seat_type = models.CharField(max_length=30, choices=SEAT_TYPE_CHOICES, default='Middle')
    is_premium = models.BooleanField(default=False)
    is_reserved = models.BooleanField(default=False)
    price_multiplier = models.DecimalField(max_digits=4, decimal_places=2, default=1.00)

    class Meta:
        unique_together = ('flight', 'seat_number')

    def __str__(self):
        return f"{self.seat_number} ({self.flight.flight_number})"

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    travel_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.flight.flight_number}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"

class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
