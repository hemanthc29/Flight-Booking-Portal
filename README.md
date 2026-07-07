# SkyZone - Django Full Stack Flight Booking Website

SkyZone is a feature-rich, high-fidelity, and responsive **Flight Booking Platform** built with HTML5, CSS3 (Space Cadet Variables), JavaScript (ES6+), Bootstrap 5, Python 3, Django, and SQLite. 

The website includes flight searching, comparing fares, seat selection maps, simulated payment processing, and PDF ticket generation with built-in QR codes.

---

## 🚀 Key Features

* **User Authentication**: Secure user registration, logins, logouts, profile edits (passport number, nationality, avatar upload), password updates, and email verification indicators.
* **Flight Search engine**: Search flights by origin, destination, departure date, passenger count, and cabin class.
* **Advanced Filters Sidebar**: Filter flights by stops, duration range, airline carriers, and price limits.
* **Interactive Seating Map**: Select or deselect seats on a grid. Seats are color-coded (Economy, Business, Premium, Aisle, Window, and Emergency exit seats highlighted).
* **Dynamic Fare Calculator**: Computes subtotal, upgrade fees, discount coupons (e.g. `STUDENT10`, `FESTIVAL50`, `EARLYBIRD`), taxes, and convenience charges on the checkout form in real time using client-side JavaScript.
* **Simulated Payments Gateway**: Checkout via Credit/Debit card, UPI QR code, or Net Banking options.
* **E-Ticket Builder**: Creates individual PDFs with custom-drawn flight schedules, passenger details, and custom QR codes containing booking logs.
* **Reviews & Ratings**: Add, edit, or delete star reviews on details cards.
* **Comparison Matrix**: Select and compare up to 3 flights side-by-side.
* **Wishlist Syncing**: Save flights to wishlist (persisted in Local Storage and synced to database).
* **Theme Manager**: Responsive design with persistent light/dark mode (saved in Local Storage).
* **Admin Statistics Console**: Custom charts and widgets displaying daily booking tallies, total revenues, monthly revenue, popular destination city rankings, and blocks/unblocks user controls.

---

## 🛠️ Setup Instructions

### 1. Install Dependencies
Make sure you have Python 3.10+ installed. Install project requirements:
```bash
pip install -r requirements.txt
```

### 2. Run Database Migrations
Create the SQLite database schema:
```bash
python manage.py makemigrations accounts flights bookings payments
python manage.py migrate
```

### 3. Seed Database Data
Load partner airports, airlines (draws PIL logos), aircraft fleets, routes, seat grids, and mock review messages:
```bash
python manage.py seed_db
```

### 4. Run Development Server
Start the Django local server:
```bash
python manage.py runserver
```
Visit the website at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🔑 Test Accounts & Logins

You can log in using these pre-seeded profiles:

* **Administrator Profile** (Access to admin dashboard at `/admin-dashboard/`):
  * **Username**: `admin`
  * **Password**: `admin123`
* **Standard Passenger Profile**:
  * **Username**: `john_doe`
  * **Password**: `pass123`
* **Additional Passenger Profile**:
  * **Username**: `jane_smith`
  * **Password**: `pass123`
