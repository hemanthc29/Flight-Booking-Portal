import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse, HttpResponseForbidden
from django.utils import timezone
from django.db.models import Q, Count, Sum, Avg
from datetime import datetime

from .models import Airline, Airport, Aircraft, Route, Flight, Seat, Review, ContactMessage, NewsletterSubscriber
from bookings.models import Booking, Passenger, Wishlist
from payments.models import Payment
from django.contrib.auth import get_user_model

User = get_user_model()

def home_view(request):
    airports = Airport.objects.all()
    airlines = Airline.objects.all()[:6]
    popular_destinations = Airport.objects.all()[:4]
    
    # Select featured flights
    featured_flights = Flight.objects.filter(departure_time__gt=timezone.now()).order_by('base_fare')[:3]
    
    # Get reviews for testimonials
    testimonials = Review.objects.all().select_related('user', 'flight').order_by('-created_at')[:3]
    
    context = {
        'airports': airports,
        'airlines': airlines,
        'popular_destinations': popular_destinations,
        'featured_flights': featured_flights,
        'testimonials': testimonials,
    }
    return render(request, 'home.html', context)

def flight_search_view(request):
    origin_code = request.GET.get('origin')
    destination_code = request.GET.get('destination')
    departure_date_str = request.GET.get('departure_date')
    return_date_str = request.GET.get('return_date')
    passengers = request.GET.get('passengers', 1)
    cabin_class = request.GET.get('cabin_class', 'Economy')
    trip_type = request.GET.get('trip_type', 'one-way')

    # Basic base query (show future flights)
    flights = Flight.objects.filter(departure_time__gt=timezone.now()).select_related('airline', 'route__origin', 'route__destination')

    # Apply search parameters
    if origin_code:
        flights = flights.filter(route__origin__code=origin_code)
    if destination_code:
        flights = flights.filter(route__destination__code=destination_code)
    if departure_date_str:
        try:
            dep_date = datetime.strptime(departure_date_str, '%Y-%m-%d').date()
            flights = flights.filter(departure_time__date=dep_date)
        except ValueError:
            pass
            
    if cabin_class:
        flights = flights.filter(cabin_class=cabin_class)

    # Filter Sidebar parameters
    direct_only = request.GET.get('direct') == 'true'
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')
    airline_code = request.GET.get('airline')
    stops_filter = request.GET.get('stops') # e.g. "0", "1"
    duration_max = request.GET.get('duration_max') # in hours

    if price_min:
        flights = flights.filter(base_fare__gte=float(price_min))
    if price_max:
        flights = flights.filter(base_fare__lte=float(price_max))
    if airline_code:
        flights = flights.filter(airline__code=airline_code)

    # Convert flights to list to calculate stops and duration filters if needed
    flight_list = []
    for f in flights:
        # Check seats availability
        available_seats_count = f.seats.filter(is_reserved=False).count()
        if available_seats_count < int(passengers):
            continue # Skip flights without enough seats
            
        stops = 0 # In our mock database, flights are direct, but we can simulate routes or stops
        if stops_filter:
            if stops_filter == '0' and stops > 0: continue
            if stops_filter == '1' and stops != 1: continue
            if stops_filter == '2' and stops < 2: continue

        dur_hours = f.duration.total_seconds() / 3600.0
        if duration_max and dur_hours > float(duration_max):
            continue
            
        flight_list.append(f)

    # Collect unique airlines and price range in current results for dynamic filters sidebar
    all_airlines = Airline.objects.all()
    airports = Airport.objects.all()

    context = {
        'flights': flight_list,
        'airlines': all_airlines,
        'airports': airports,
        'origin_code': origin_code,
        'destination_code': destination_code,
        'departure_date': departure_date_str,
        'return_date': return_date_str,
        'passengers': passengers,
        'cabin_class': cabin_class,
        'trip_type': trip_type,
    }
    return render(request, 'flight_search.html', context)

def flight_details_view(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    seats = flight.seats.all().order_by('seat_number')
    reviews = flight.reviews.all().select_related('user').order_by('-created_at')
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0
    
    context = {
        'flight': flight,
        'seats': seats,
        'reviews': reviews,
        'avg_rating': round(avg_rating, 1),
    }
    return render(request, 'flight_details.html', context)

@login_required
def add_review_view(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        travel_date = request.POST.get('travel_date') or timezone.now().date()
        
        Review.objects.create(
            user=request.user,
            flight=flight,
            rating=int(rating),
            comment=comment,
            travel_date=travel_date
        )
        messages.success(request, "Thank you for reviewing this flight!")
    return redirect('flights:details', flight_id=flight.id)

@login_required
def edit_review_view(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if review.user != request.user:
        return HttpResponseForbidden("You cannot edit this review.")
        
    if request.method == 'POST':
        review.rating = int(request.POST.get('rating'))
        review.comment = request.POST.get('comment')
        review.save()
        messages.success(request, "Review updated successfully!")
    return redirect('flights:details', flight_id=review.flight.id)

@login_required
def delete_review_view(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if review.user != request.user and not request.user.is_staff:
        return HttpResponseForbidden("You cannot delete this review.")
        
    flight_id = review.flight.id
    review.delete()
    messages.success(request, "Review deleted successfully!")
    return redirect('flights:details', flight_id=flight_id)

def wishlist_view(request):
    wishlisted_flights = []
    if request.user.is_authenticated:
        db_wishlist = Wishlist.objects.filter(user=request.user).select_related('flight__airline', 'flight__route__origin', 'flight__route__destination')
        wishlisted_flights = [w.flight for w in db_wishlist]
    return render(request, 'wishlist.html', {'flights': wishlisted_flights})

def wishlist_sync_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({'status': 'unauthorized'}, status=401)
        
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            flight_id = data.get('flight_id')
            action = data.get('action')
            
            flight = Flight.objects.get(id=flight_id)
            if action == 'add':
                Wishlist.objects.get_or_create(user=request.user, flight=flight)
                return JsonResponse({'status': 'added'})
            elif action == 'remove':
                Wishlist.objects.filter(user=request.user, flight=flight).delete()
                return JsonResponse({'status': 'removed'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'bad_request'}, status=400)

def flight_compare_view(request):
    ids_str = request.GET.get('ids', '')
    if not ids_str:
        messages.warning(request, "Please select flights to compare.")
        return redirect('flights:search')
        
    ids = [int(i) for i in ids_str.split(',') if i.isdigit()]
    flights = Flight.objects.filter(id__in=ids).select_related('airline', 'route__origin', 'route__destination')
    
    # Calculate average ratings
    ratings = {}
    for f in flights:
        avg = f.reviews.aggregate(Avg('rating'))['rating__avg']
        ratings[f.id] = round(avg, 1) if avg else 'No ratings'

    return render(request, 'wishlist.html', {
        'compare_flights': flights,
        'ratings': ratings
    })

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        ContactMessage.objects.create(name=name, email=email, subject=subject, message=message)
        messages.success(request, "Your contact message has been sent successfully!")
        return redirect('flights:contact')
    return render(request, 'contact.html')

def faq_view(request):
    return render(request, 'faq.html')

def airports_view(request):
    airports = Airport.objects.all()
    return render(request, 'about.html', {'airports': airports})

def airlines_view(request):
    airlines = Airline.objects.all()
    return render(request, 'about.html', {'airlines': airlines})

def offers_view(request):
    return render(request, 'about.html', {'offers': True})

def newsletter_subscribe_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            NewsletterSubscriber.objects.get_or_create(email=email)
            messages.success(request, "Thank you for subscribing to our newsletter!")
        else:
            messages.error(request, "Invalid email address.")
    return redirect(request.META.get('HTTP_REFERER', 'flights:home'))

@login_required
def admin_dashboard_view(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("Access Denied.")
        
    # Analytics Data
    today = timezone.now().date()
    daily_bookings_count = Booking.objects.filter(booking_date__date=today).count()
    
    total_revenue = Booking.objects.filter(status='Confirmed').aggregate(Sum('total_amount'))['total_amount__sum'] or 0
    
    # Group bookings by route destination city
    popular_destinations = Booking.objects.filter(status='Confirmed')\
        .values('flight__route__destination__city')\
        .annotate(count=Count('id'))\
        .order_by('-count')[:5]
        
    # Group bookings by airline
    most_booked_airlines = Booking.objects.filter(status='Confirmed')\
        .values('flight__airline__name')\
        .annotate(count=Count('id'))\
        .order_by('-count')[:5]
        
    # Monthly revenue groupings
    monthly_revenue = Booking.objects.filter(status='Confirmed')\
        .values('booking_date__month')\
        .annotate(revenue=Sum('total_amount'), count=Count('id'))\
        .order_by('booking_date__month')

    # Data lists for crud management
    all_flights = Flight.objects.all().select_related('airline', 'route__origin', 'route__destination')
    all_bookings = Booking.objects.all().select_related('user', 'flight').order_by('-booking_date')
    all_users = User.objects.all().order_by('-date_joined')
    all_payments = Payment.objects.all().select_related('booking__user')

    context = {
        'daily_bookings': daily_bookings_count,
        'total_revenue': total_revenue,
        'popular_destinations': popular_destinations,
        'most_booked_airlines': most_booked_airlines,
        'monthly_revenue': monthly_revenue,
        'flights': all_flights,
        'bookings': all_bookings,
        'users': all_users,
        'payments': all_payments
    }
    return render(request, 'admin_dashboard.html', context)

@login_required
def admin_block_user_view(request, user_id):
    if not request.user.is_staff:
        return HttpResponseForbidden()
    target_user = get_object_or_404(User, id=user_id)
    if target_user.is_superuser:
        messages.error(request, "Cannot block superusers.")
    else:
        target_user.is_active = not target_user.is_active
        target_user.save()
        status_str = "blocked" if not target_user.is_active else "unblocked"
        messages.success(request, f"User {target_user.username} has been {status_str}.")
    return redirect('flights:admin_dashboard')

@login_required
def admin_delete_user_view(request, user_id):
    if not request.user.is_staff:
        return HttpResponseForbidden()
    target_user = get_object_or_404(User, id=user_id)
    if target_user.is_superuser:
        messages.error(request, "Cannot delete superusers.")
    else:
        target_user.delete()
        messages.success(request, "User deleted successfully.")
    return redirect('flights:admin_dashboard')

@login_required
def admin_refund_booking_view(request, booking_id):
    if not request.user.is_staff:
        return HttpResponseForbidden()
    booking = get_object_or_404(Booking, id=booking_id)
    if hasattr(booking, 'payment'):
        payment = booking.payment
        payment.status = 'Refunded'
        payment.save()
    booking.status = 'Cancelled'
    booking.save()
    
    # Release seats
    for p in booking.passengers.all():
        if p.seat:
            p.seat.is_reserved = False
            p.seat.save()
            
    messages.success(request, f"Refund approved for booking {booking.pnr}.")
    return redirect('flights:admin_dashboard')

@login_required
def admin_cancel_booking_view(request, booking_id):
    if not request.user.is_staff:
        return HttpResponseForbidden()
    booking = get_object_or_404(Booking, id=booking_id)
    booking.status = 'Cancelled'
    booking.save()
    
    # Release seats
    for p in booking.passengers.all():
        if p.seat:
            p.seat.is_reserved = False
            p.seat.save()
            
    messages.success(request, f"Booking {booking.pnr} cancelled successfully.")
    return redirect('flights:admin_dashboard')
