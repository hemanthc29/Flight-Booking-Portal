import random
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

from bookings.models import Booking
from bookings.ticket_utils import generate_ticket_assets
from .models import Payment, Ticket

@login_required
def process_payment_view(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    # If already confirmed, redirect to confirmation directly
    if booking.status == 'Confirmed':
        return redirect('payments:confirmation', booking_id=booking.id)

    if request.method == 'POST':
        payment_method = request.POST.get('payment_method', 'Credit Card')
        
        # Simulate payment gateway authorization
        txn_pool = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        transaction_id = "TXN-" + "".join(random.choice(txn_pool) for _ in range(12))
        
        # Create Payment Record
        payment = Payment.objects.create(
            booking=booking,
            transaction_id=transaction_id,
            payment_method=payment_method,
            amount=booking.total_amount,
            status='Successful'
        )
        
        # Update Booking Status
        booking.status = 'Confirmed'
        booking.save()
        
        # 3. Generate tickets (PDF + QR code) for each passenger
        for passenger in booking.passengers.all():
            generate_ticket_assets(booking, passenger)
            
        messages.success(request, f"Payment authorized! Your tickets have been issued successfully.")
        return redirect('payments:confirmation', booking_id=booking.id)

    return render(request, 'payment.html', {'booking': booking})

@login_required
def payment_confirmation_view(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    tickets = Ticket.objects.filter(booking=booking).select_related('passenger')
    
    return render(request, 'confirmation.html', {
        'booking': booking,
        'tickets': tickets
    })
