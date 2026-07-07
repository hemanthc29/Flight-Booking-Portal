import os
import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from django.conf import settings
from django.utils import timezone
from django.contrib.auth import get_user_model

# Import models
from flights.models import Airline, Airport, Aircraft, Route, Flight, Seat, Review
from bookings.models import Booking, Passenger

User = get_user_model()

class Command(BaseCommand):
    help = 'Seeds the database with test data for flight bookings'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding database...')
        
        # Ensure media folders exist
        os.makedirs(os.path.join(settings.MEDIA_ROOT, 'airline_logos'), exist_ok=True)
        os.makedirs(os.path.join(settings.MEDIA_ROOT, 'tickets'), exist_ok=True)
        os.makedirs(os.path.join(settings.MEDIA_ROOT, 'profile_pictures'), exist_ok=True)

        # 1. Create Users
        self.stdout.write('Creating users...')
        admin_user, created = User.objects.get_or_create(
            username='admin',
            email='admin@flightbooking.com',
            is_staff=True,
            is_superuser=True
        )
        if created:
            admin_user.set_password('admin123')
            admin_user.save()

        test_users = []
        user_data = [
            ('john_doe', 'john@gmail.com', 'John', 'Doe', 'US123456', 'American'),
            ('jane_smith', 'jane@gmail.com', 'Jane', 'Smith', 'UK987654', 'British'),
            ('alex_traveler', 'alex@gmail.com', 'Alex', 'Rider', 'IN456789', 'Indian'),
        ]
        for username, email, first, last, passport, nationality in user_data:
            user, created = User.objects.get_or_create(
                username=username,
                email=email,
                first_name=first,
                last_name=last,
                passport_number=passport,
                nationality=nationality,
                email_verified=True
            )
            if created:
                user.set_password('pass123')
                user.save()
            test_users.append(user)

        # Helper to generate simple colored logos with Pillow
        def generate_mock_logo(name, filename, color):
            try:
                from PIL import Image, ImageDraw, ImageFont
                # Create a solid color image
                img = Image.new('RGB', (100, 100), color=color)
                draw = ImageDraw.Draw(img)
                # Draw simple text letter
                draw.text((35, 30), name[:2].upper(), fill=(255, 255, 255))
                
                logo_path = os.path.join(settings.MEDIA_ROOT, 'airline_logos', filename)
                img.save(logo_path)
                return f'airline_logos/{filename}'
            except Exception as e:
                self.stdout.write(f"PIL logo generation skipped: {e}")
                return None

        # 2. Create Airlines
        self.stdout.write('Creating airlines...')
        airlines_data = [
            ('SkyWays Airline', 'SW', '#6366f1'),
            ('GlobalJet Express', 'GJ', '#06b6d4'),
            ('OceanAir Airways', 'OA', '#10b981'),
            ('Emirates Connect', 'EK', '#ef4444'),
            ('British Flyer', 'BF', '#f59e0b'),
        ]
        airlines = []
        for name, code, color in airlines_data:
            logo_filename = f"{code.lower()}_logo.png"
            logo_path = generate_mock_logo(name, logo_filename, color)
            
            airline, _ = Airline.objects.get_or_create(
                code=code,
                defaults={
                    'name': name,
                    'logo': logo_path,
                    'contact_details': f'Support: support@{code.lower()}.com | +1 800 {code}',
                    'fleet_details': 'Operating Boeing 777s, Airbus A320s, and Boeing 737s.'
                }
            )
            airlines.append(airline)

        # 3. Create Airports
        self.stdout.write('Creating airports...')
        airports_data = [
            ('JFK', 'John F. Kennedy International', 'New York', 'USA', 'Terminal 4 & 7. Support: +1 718-244-4444. Maps: JFK Airport', 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m12!1m3!1d12108.647310340156!2d-73.79124439009848!3d40.64131108253139!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c26650d5404947%3A0xec4fa6b3460cf854!2sJohn%20F.%20Kennedy%20International%20Airport!5e0!3m2!1sen!2sus!4v1700000000000!5m2!1sen!2sus'),
            ('LAX', 'Los Angeles International', 'Los Angeles', 'USA', 'Tom Bradley International Terminal. Support: +1 310-646-5252.', 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m12!1m3!1d13247.925482390887!2d-118.42398544837593!3d33.94158889814407!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x80c2b0d213b28fb5%3A0x77a87b57698badf1!2sLos%20Angeles%20International%20Airport!5e0!3m2!1sen!2sus!4v1700000000000!5m2!1sen!2sus'),
            ('LHR', 'London Heathrow Airport', 'London', 'UK', 'Terminal 2, 3 & 5. Support: +44 844 335 1801.', 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m12!1m3!1d12423.821102931566!2d-0.4619379878233306!3d51.47002229562725!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x48767234cdc56c8b%3A0xbe47918a28e9324c!2sHeathrow%20Airport!5e0!3m2!1sen!2suk!4v1700000000000!5m2!1sen!2suk'),
            ('DXB', 'Dubai International', 'Dubai', 'UAE', 'Terminal 3 (Emirates). Support: +971 4 224 5555.', 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m12!1m3!1d14434.908075306394!2d55.35338304910246!3d25.252441996535565!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3e5f5c165eb393fb%3A0x67dbad97a3cfad2d!2sDubai%20International%20Airport!5e0!3m2!1sen!2sae!4v1700000000000!5m2!1sen!2sae'),
            ('CDG', 'Charles de Gaulle Airport', 'Paris', 'France', 'Terminal 2E & 2F. Support: +33 1 70 36 39 50.', 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m12!1m3!1d13083.565860717462!2d2.535876548767676!3d49.00969068067812!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47e614d9b6264ff3%3A0xbe97a22bf445bb96!2sParis%20Charles%20de%20Gaulle%20Airport!5e0!3m2!1sen!2sfr!4v1700000000000!5m2!1sen!2sfr'),
            ('BOM', 'Chhatrapati Shivaji Maharaj International', 'Mumbai', 'India', 'Terminal 2. Support: +91 22 6685 1010.', 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m12!1m3!1d15082.973347098485!2d72.86318995079633!3d19.08955959955745!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3be7c86e24614e55%3A0x7d8753cd84d94348!2sChhatrapati%20Shivaji%20Maharaj%20International%20Airport%20Mumbai!5e0!3m2!1sen!2sin!4v1700000000000!5m2!1sen!2sin'),
        ]
        airports = {}
        for code, name, city, country, terminal, map_url in airports_data:
            airport, _ = Airport.objects.get_or_create(
                code=code,
                defaults={
                    'name': name,
                    'city': city,
                    'country': country,
                    'terminal_info': terminal,
                    'contact_details': f'Airport Support: +99 {code} INFO',
                    'map_embed_url': map_url
                }
            )
            airports[code] = airport

        # 4. Create Aircrafts
        self.stdout.write('Creating aircrafts...')
        aircraft_data = [
            ('777-300ER', 'Boeing', 300),
            ('A320neo', 'Airbus', 150),
            ('737 MAX 9', 'Boeing', 180),
        ]
        aircrafts = []
        for model, manufacturer, capacity in aircraft_data:
            aircraft, _ = Aircraft.objects.get_or_create(
                model_name=model,
                manufacturer=manufacturer,
                capacity=capacity
            )
            aircrafts.append(aircraft)

        # 5. Create Routes
        self.stdout.write('Creating routes...')
        routes_data = [
            ('JFK', 'LAX', 3975, timedelta(hours=6)),
            ('LAX', 'JFK', 3975, timedelta(hours=5, minutes=30)),
            ('JFK', 'LHR', 5570, timedelta(hours=7, minutes=15)),
            ('LHR', 'JFK', 5570, timedelta(hours=8)),
            ('DXB', 'BOM', 1930, timedelta(hours=3, minutes=30)),
            ('BOM', 'DXB', 1930, timedelta(hours=3, minutes=45)),
            ('CDG', 'JFK', 5835, timedelta(hours=8, minutes=30)),
            ('JFK', 'CDG', 5835, timedelta(hours=7, minutes=45)),
            ('LHR', 'DXB', 5470, timedelta(hours=7)),
            ('DXB', 'LHR', 5470, timedelta(hours=7, minutes=45)),
        ]
        routes = []
        for orig_code, dest_code, dist, dur in routes_data:
            route, _ = Route.objects.get_or_create(
                origin=airports[orig_code],
                destination=airports[dest_code],
                defaults={'distance': dist, 'duration': dur}
            )
            routes.append(route)

        # 6. Create Flights & Seats
        self.stdout.write('Creating flights and seat maps...')
        now = timezone.now()
        flight_counter = 100
        
        # We will create flights spanning the next 10 days
        for day in range(11):
            date_offset = now + timedelta(days=day)
            for r in routes:
                # Randomize airline and aircraft
                airline = random.choice(airlines)
                aircraft = random.choice(aircrafts)
                
                # Base fare between $150 and $850 based on route distance
                dist_factor = float(r.distance) / 1000.0
                base_fare = round(dist_factor * 120.0 + random.uniform(50, 150), 2)
                
                # Determine departure time (say 8 AM and 4 PM)
                for departure_hour in [8, 16]:
                    flight_num = f"{airline.code}{flight_counter}"
                    flight_counter += 1
                    
                    dept_time = timezone.make_aware(datetime(
                        date_offset.year, date_offset.month, date_offset.day,
                        departure_hour, 0
                    ))
                    arr_time = dept_time + r.duration
                    
                    for cabin in ['Economy', 'Business', 'First']:
                        flight, created = Flight.objects.get_or_create(
                            flight_number=f"{flight_num}-{cabin[0]}",
                            defaults={
                                'airline': airline,
                                'aircraft': aircraft,
                                'route': r,
                                'departure_time': dept_time,
                                'arrival_time': arr_time,
                                'base_fare': base_fare if cabin == 'Economy' else (base_fare * 2.0 if cabin == 'Business' else base_fare * 3.5),
                                'cabin_class': cabin,
                                'status': 'Scheduled',
                                'baggage_allowance': '30kg check-in, 7kg cabin' if cabin != 'Economy' else '15kg check-in, 7kg cabin',
                                'meals_included': True if cabin != 'Economy' else random.choice([True, False])
                            }
                        )
                        
                        if created:
                            # Generate a Grid of Seats for this flight
                            # Columns A, B (Window, Aisle/Middle), C, D, E, F
                            # Rows 1 to 5 (First Class: Row 1, Business: Row 2, Economy: Row 3-5)
                            seats_to_create = []
                            for row in range(1, 6):
                                for col in ['A', 'B', 'C', 'D', 'E', 'F']:
                                    seat_num = f"{row}{col}"
                                    
                                    # Class mapping
                                    s_class = 'First' if row == 1 else ('Business' if row == 2 else 'Economy')
                                    
                                    # Type mapping
                                    if col in ['A', 'F']:
                                        s_type = 'Window'
                                    elif col in ['C', 'D']:
                                        s_type = 'Aisle'
                                    else:
                                        s_type = 'Middle'
                                        
                                    if row == 3:
                                        s_type = 'Emergency Exit'
                                        
                                    is_premium = s_class in ['First', 'Business'] or s_type == 'Emergency Exit'
                                    
                                    # Price Multiplier
                                    mult = 1.00
                                    if s_class == 'First':
                                        mult = 1.80
                                    elif s_class == 'Business':
                                        mult = 1.40
                                    elif s_type == 'Emergency Exit':
                                        mult = 1.20
                                    elif s_type == 'Window':
                                        mult = 1.10
                                        
                                    # Randomize occupancy for demonstration
                                    is_res = random.choice([True, False, False, False]) # 25% chance reserved
                                    
                                    seats_to_create.append(Seat(
                                        flight=flight,
                                        seat_number=seat_num,
                                        seat_class=s_class,
                                        seat_type=s_type,
                                        is_premium=is_premium,
                                        is_reserved=is_res,
                                        price_multiplier=mult
                                    ))
                            Seat.objects.bulk_create(seats_to_create)

        # 7. Create Reviews
        self.stdout.write('Creating flight reviews...')
        all_flights = Flight.objects.all()
        comments = [
            "Amazing service! Very punctual and comfortable seats.",
            "Average flight. The meal option was poor, but staff was polite.",
            "Legroom in Economy was tight, but flight was smooth and on-time.",
            "Absolutely premium experience in First Class. Exquisite food!",
            "Slightly delayed departure, but the captain flew beautifully to make up time."
        ]
        
        for user in test_users:
            # Pick 3 random flights to review
            for f in random.sample(list(all_flights), 3):
                Review.objects.create(
                    user=user,
                    flight=f,
                    rating=random.randint(3, 5),
                    comment=random.choice(comments),
                    travel_date=now.date() - timedelta(days=random.randint(1, 10))
                )

        self.stdout.write(self.style.SUCCESS('Successfully seeded flight booking database!'))
