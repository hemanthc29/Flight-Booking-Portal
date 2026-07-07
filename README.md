# SkyZone Flight Booking Website

SkyZone is a modern, responsive, and high-fidelity Flight Booking Website built using pure HTML, Vanilla CSS, and Vanilla JavaScript. Designed for the Python-FSD curriculum, it provides passengers with a premium, seamless digital booking experience.

## 🚀 Key Features

- **✈️ Hero Flight Search Widget**: Search flights by Origin, Destination, Dates (Departure & Return for Round Trip), Traveller count, and Travel Class (Economy, Premium Economy, Business, First Class). Includes client-side date checks (prevents past dates or return dates before departure).
- **🎨 Glassmorphic Dark/Light Mode Theme**: Fully functional theme toggler with preferences persisted in `localStorage`.
- **🔍 Sidebar Filtering & Sorting**: Filter available flights by maximum price, number of stops, and airlines. Sort results by cheapest flight fare or fastest flight duration.
- **💺 Interactive Seat Map Cabin**: Visual seat grid (Window, Aisle, Middle, Emergency Exit Row) showing Available, Selected, and Reserved statuses. Selecting Exit Row seats dynamically calculates a premium surcharge.
- **📝 Passenger Info validation**: Dynamic passenger detail inputs based on passenger counts with email format and passport regex validations.
- **💳 Fare Surcharge Calculator**: Instantly updates Base Fare, Seat Upgrades, Taxes, Baggage Surcharges, Promo Discounts, and Grand Total when selection options are changed.
- **🎁 Coupon Discounts**: Apply voucher codes like `EARLY10` (10% off), `FESTIVAL15` (15% off), or `STUDENT20` (20% off) for instant checkout deductions. Includes a live expiry countdown timer on the Offers page.
- **🎫 Print-Ready Boarding Passes**: Displays purchased flight histories in "My Bookings" with barcode rendering, boarding pass graphics, cancellation support, and window print-friendly CSS.
- **❔ Accordion FAQs & Baggage Info**: Fast-responsive Accordion FAQs, Cabin/Check-in weight guidelines, and prohibited baggage warnings.

---

## 📁 Project Folder Structure

```text
Flight-Booking-Website/
├── index.html                 # Home / Main search landing page
├── style.css                  # Premium CSS custom tokens & transitions
├── script.js                  # Central flight dataset & page state controller
├── assets/
│   ├── images/
│   │   ├── banners/
│   │   │   └── hero.webp      # Sunrise airplane banner generated via AI
│   │   ├── airlines/
│   │   ├── destinations/
│   │   └── icons/
│   ├── videos/
│   └── fonts/
├── pages/
│   ├── flights.html           # Available flights list and filter sidebar
│   ├── seat-selection.html    # Airplane interactive seat layout map
│   ├── booking.html           # Passenger details checkout page
│   ├── offers.html            # Promotional coupons with countdown timers
│   ├── my-bookings.html       # Completed passes and cancellation panel
│   ├── about.html             # FAQ Accordion and baggage rules details
│   └── contact.html           # Contact forms & helpline numbers
└── README.md                  # Project documentation info
```

---

## 💻 Tech Stack & Design Architecture

- **Core Structure**: Semantic HTML5 tags.
- **Visual Design**: CSS Custom Variables, modern flexbox/grid alignments, responsive media query breakpoints (optimized for mobile, tablet, and desktop), keyframe hover animations, and FontAwesome CDNs.
- **Logical Flow**: State variables stored and updated across multiple pages using the web browser's `localStorage` (Theme Preference, Current Search Parameters, Active Booking state, Booking History list, and Bookmarked/Favorite flights).

---

## 🛠️ How to Run Locally

1. Clone or copy this project workspace onto your local machine.
2. Double-click `index.html` to open the website directly in any modern web browser (Google Chrome, Microsoft Edge, Mozilla Firefox, Safari).
3. Switch on **Dark Theme** by clicking the moon icon in the navigation bar.
4. Try booking a flight:
   - Search for a flight from **New York** to **London**.
   - Pick a flight on the listing page.
   - Choose emergency Exit seats (Row 5) to see fare updates.
   - Apply discount coupon code **STUDENT20** during checkout.
   - Verify that your booking ID is generated and ticket appears in your **My Bookings** tab.
