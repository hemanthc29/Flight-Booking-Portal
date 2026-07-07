from django.db import models
from bookings.models import Booking, Passenger

class Payment(models.Model):
    METHOD_CHOICES = (
        ('Credit Card', 'Credit Card'),
        ('Debit Card', 'Debit Card'),
        ('UPI', 'UPI'),
        ('Net Banking', 'Net Banking'),
        ('Digital Wallet', 'Digital Wallet'),
    )
    STATUS_CHOICES = (
        ('Successful', 'Successful'),
        ('Failed', 'Failed'),
        ('Refunded', 'Refunded'),
    )

    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name='payment')
    transaction_id = models.CharField(max_length=100, unique=True)
    payment_method = models.CharField(max_length=50, choices=METHOD_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Successful')

    def __str__(self):
        return f"Payment {self.transaction_id} for booking {self.booking.pnr} ({self.status})"

class Ticket(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='tickets')
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE, related_name='tickets')
    ticket_number = models.CharField(max_length=50, unique=True)
    pdf_file = models.FileField(upload_to='tickets/', blank=True, null=True)
    qr_code = models.ImageField(upload_to='tickets/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ticket {self.ticket_number} for passenger {self.passenger.first_name} {self.passenger.last_name}"
