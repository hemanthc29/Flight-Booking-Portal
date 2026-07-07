import random
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, Http404
from django.utils import timezone
from django.conf import settings

from .models import Booking, Passenger
from flights.models import Flight, Seat
from payments.models import Ticket

@login_required
def book_flight_view(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    available_seats = flight.seats.filter(is_reserved=False)
    
    if request.method == 'POST':
        # Retrieve arrays of passenger details from multi-passenger form
        first_names = request.POST.getlist('first_name')
        last_names = request.POST.getlist('last_name')
        ages = request.POST.getlist('age')
        genders = request.POST.getlist('gender')
        passports = request.POST.getlist('passport_number')
        nationalities = request.POST.getlist('nationality')
        selected_seat_ids = request.POST.getlist('seat_id') # IDs of selected seats
        special_requests_list = request.POST.getlist('special_requests')

        # Form validations
        if not first_names or len(first_names) == 0:
            messages.error(request, "Please enter details for at least one passenger.")
            return redirect('bookings:book_flight', flight_id=flight.id)

        # Generate a random 6-character alphanumeric PNR
        char_pool = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
        pnr = "".join(random.choice(char_pool) for _ in range(6))
        while Booking.objects.filter(pnr=pnr).exists():
            pnr = "".join(random.choice(char_pool) for _ in range(6))

        # Calculate Fare Elements
        passenger_count = len(first_names)
        base_fare_total = flight.base_fare * passenger_count
        
        # Calculate convenience fee and taxes
        convenience_fee = 20.00
        taxes = float(base_fare_total) * 0.10 # 10% tax
        
        # Coupon Discounts
        coupon_code = request.POST.get('coupon_code', '').strip().upper()
        discount = 0.00
        if coupon_code == 'STUDENT10':
            discount = float(base_fare_total) * 0.10
        elif coupon_code == 'FESTIVAL50':
            discount = min(50.00, float(base_fare_total))
        elif coupon_code == 'EARLYBIRD':
            discount = float(base_fare_total) * 0.15

        total_amount = float(base_fare_total) + taxes + convenience_fee - discount
        if total_amount < 0:
            total_amount = 0

        # Create Booking
        booking = Booking.objects.create(
            user=request.user,
            flight=flight,
            pnr=pnr,
            status='Pending',
            total_amount=total_amount
        )

        # Process and save each passenger
        for i in range(passenger_count):
            seat_obj = None
            if i < len(selected_seat_ids) and selected_seat_ids[i]:
                try:
                    seat_obj = Seat.objects.get(id=int(selected_seat_ids[i]), flight=flight)
                    seat_obj.is_reserved = True
                    seat_obj.save()
                except Seat.DoesNotExist:
                    pass

            Passenger.objects.create(
                booking=booking,
                first_name=first_names[i],
                last_name=last_names[i],
                age=int(ages[i]) if ages[i].isdigit() else 30,
                gender=genders[i] if i < len(genders) else 'Male',
                passport_number=passports[i] if i < len(passports) else '',
                nationality=nationalities[i] if i < len(nationalities) else '',
                seat=seat_obj,
                special_requests=special_requests_list[i] if i < len(special_requests_list) else ''
            )

        messages.success(request, f"Booking draft saved! Please complete your payment for PNR {pnr}.")
        return redirect('payments:process_payment', booking_id=booking.id)

    # Context for rendering form
    seats = flight.seats.all().order_by('seat_number')
    return render(request, 'booking.html', {
        'flight': flight,
        'available_seats': available_seats,
        'seats': seats
    })

@login_required
def my_bookings_view(request):
    bookings = Booking.objects.filter(user=request.user).select_related('flight__airline', 'flight__route__origin', 'flight__route__destination').order_by('-booking_date')
    return render(request, 'my_bookings.html', {'bookings': bookings})

@login_required
def cancel_booking_view(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if booking.status == 'Cancelled':
        messages.warning(request, "This booking has already been cancelled.")
        return redirect('bookings:my_bookings')

    # Release passenger seats
    for passenger in booking.passengers.all():
        if passenger.seat:
            passenger.seat.is_reserved = False
            passenger.seat.save()

    # Update Booking and Payment
    booking.status = 'Cancelled'
    booking.save()

    if hasattr(booking, 'payment'):
        payment = booking.payment
        payment.status = 'Refunded'
        payment.save()
        messages.success(request, f"Booking {booking.pnr} cancelled. Refund of ${booking.total_amount} processed.")
    else:
        messages.success(request, f"Booking {booking.pnr} cancelled successfully.")

    return redirect('bookings:my_bookings')

@login_required
def download_ticket_view(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, booking__user=request.user)
    if not ticket.pdf_file:
        raise Http404("Ticket file not generated.")
        
    response = HttpResponse(ticket.pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="ticket_{ticket.ticket_number}.pdf"'
    return response
