// MOCK DATASET FOR FLIGHTS
const MOCK_FLIGHTS = [
    {
        id: "FL-101",
        airlineName: "Horizon Airways",
        airlineCode: "HZ",
        flightNumber: "HZ-302",
        logoColor: "#6366f1", // Indigo
        fromCity: "New York",
        fromCode: "JFK",
        toCity: "London",
        toCode: "LHR",
        depTime: "08:30 AM",
        arrTime: "08:45 PM",
        duration: "7h 15m",
        stops: 0,
        price: 450,
        seatsAvailable: 8,
        mealAvailable: true,
        wifiAvailable: true,
        aircraftType: "Boeing 787-9 Dreamliner",
        terminal: "Terminal 4",
        gate: "Gate A22",
        baggageCabin: "7 kg",
        baggageCheckIn: "23 kg"
    },
    {
        id: "FL-102",
        airlineName: "Horizon Airways",
        airlineCode: "HZ",
        flightNumber: "HZ-305",
        logoColor: "#6366f1",
        fromCity: "London",
        fromCode: "LHR",
        toCity: "Paris",
        toCode: "CDG",
        depTime: "10:15 AM",
        arrTime: "11:35 AM",
        duration: "1h 20m",
        stops: 0,
        price: 95,
        seatsAvailable: 15,
        mealAvailable: false,
        wifiAvailable: true,
        aircraftType: "Airbus A320neo",
        terminal: "Terminal 2",
        gate: "Gate B10",
        baggageCabin: "7 kg",
        baggageCheckIn: "15 kg"
    },
    {
        id: "FL-103",
        airlineName: "JetStream Express",
        airlineCode: "JS",
        flightNumber: "JS-109",
        logoColor: "#06b6d4", // Cyan
        fromCity: "Dubai",
        fromCode: "DXB",
        toCity: "Singapore",
        toCode: "SIN",
        depTime: "11:45 PM",
        arrTime: "11:15 AM",
        duration: "7h 30m",
        stops: 0,
        price: 320,
        seatsAvailable: 4,
        mealAvailable: true,
        wifiAvailable: true,
        aircraftType: "Airbus A350-900",
        terminal: "Terminal 3",
        gate: "Gate C05",
        baggageCabin: "7 kg",
        baggageCheckIn: "30 kg"
    },
    {
        id: "FL-104",
        airlineName: "Oceanic Air",
        airlineCode: "OC",
        flightNumber: "OC-815",
        logoColor: "#f59e0b", // Amber
        fromCity: "Tokyo",
        fromCode: "HND",
        toCity: "Sydney",
        toCode: "SYD",
        depTime: "09:30 PM",
        arrTime: "08:45 AM",
        duration: "10h 15m",
        stops: 1,
        price: 580,
        seatsAvailable: 2,
        mealAvailable: true,
        wifiAvailable: false,
        aircraftType: "Boeing 777-300ER",
        terminal: "Terminal 1",
        gate: "Gate 14",
        baggageCabin: "7 kg",
        baggageCheckIn: "23 kg"
    },
    {
        id: "FL-105",
        airlineName: "StarLink Aviation",
        airlineCode: "SL",
        flightNumber: "SL-501",
        logoColor: "#10b981", // Emerald
        fromCity: "New York",
        fromCode: "JFK",
        toCity: "London",
        toCode: "LHR",
        depTime: "06:15 PM",
        arrTime: "06:30 AM",
        duration: "7h 15m",
        stops: 0,
        price: 520,
        seatsAvailable: 12,
        mealAvailable: true,
        wifiAvailable: true,
        aircraftType: "Airbus A380",
        terminal: "Terminal 7",
        gate: "Gate B1",
        baggageCabin: "10 kg",
        baggageCheckIn: "32 kg"
    },
    {
        id: "FL-106",
        airlineName: "Apex Carriers",
        airlineCode: "AC",
        flightNumber: "AC-404",
        logoColor: "#ec4899", // Pink
        fromCity: "Bangkok",
        fromCode: "BKK",
        toCity: "Singapore",
        toCode: "SIN",
        depTime: "02:20 PM",
        arrTime: "05:45 PM",
        duration: "2h 25m",
        stops: 0,
        price: 110,
        seatsAvailable: 18,
        mealAvailable: true,
        wifiAvailable: false,
        aircraftType: "Boeing 737 MAX 8",
        terminal: "Terminal Main",
        gate: "Gate D6",
        baggageCabin: "7 kg",
        baggageCheckIn: "20 kg"
    },
    {
        id: "FL-107",
        airlineName: "JetStream Express",
        airlineCode: "JS",
        flightNumber: "JS-212",
        logoColor: "#06b6d4",
        fromCity: "Singapore",
        fromCode: "SIN",
        toCity: "Dubai",
        toCode: "DXB",
        depTime: "07:40 AM",
        arrTime: "11:10 AM",
        duration: "7h 30m",
        stops: 1,
        price: 360,
        seatsAvailable: 7,
        mealAvailable: true,
        wifiAvailable: true,
        aircraftType: "Airbus A350-900",
        terminal: "Terminal 1",
        gate: "Gate C18",
        baggageCabin: "7 kg",
        baggageCheckIn: "30 kg"
    },
    {
        id: "FL-108",
        airlineName: "Horizon Airways",
        airlineCode: "HZ",
        flightNumber: "HZ-808",
        logoColor: "#6366f1",
        fromCity: "Sydney",
        fromCode: "SYD",
        toCity: "Tokyo",
        toCode: "HND",
        depTime: "10:00 AM",
        arrTime: "07:30 PM",
        duration: "10h 30m",
        stops: 0,
        price: 610,
        seatsAvailable: 5,
        mealAvailable: true,
        wifiAvailable: true,
        aircraftType: "Boeing 787-9 Dreamliner",
        terminal: "Terminal International",
        gate: "Gate 24",
        baggageCabin: "7 kg",
        baggageCheckIn: "23 kg"
    },
    {
        id: "FL-109",
        airlineName: "Oceanic Air",
        airlineCode: "OC",
        flightNumber: "OC-747",
        logoColor: "#f59e0b",
        fromCity: "Paris",
        fromCode: "CDG",
        toCity: "New York",
        toCode: "JFK",
        depTime: "01:30 PM",
        arrTime: "04:00 PM",
        duration: "8h 30m",
        stops: 0,
        price: 490,
        seatsAvailable: 3,
        mealAvailable: true,
        wifiAvailable: true,
        aircraftType: "Boeing 777-300ER",
        terminal: "Terminal 2E",
        gate: "Gate K35",
        baggageCabin: "7 kg",
        baggageCheckIn: "23 kg"
    },
    {
        id: "FL-110",
        airlineName: "Apex Carriers",
        airlineCode: "AC",
        flightNumber: "AC-112",
        logoColor: "#ec4899",
        fromCity: "Singapore",
        fromCode: "SIN",
        toCity: "Bangkok",
        toCode: "BKK",
        depTime: "09:00 AM",
        arrTime: "10:30 AM",
        duration: "2h 30m",
        stops: 0,
        price: 115,
        seatsAvailable: 14,
        mealAvailable: false,
        wifiAvailable: false,
        aircraftType: "Boeing 737 MAX 8",
        terminal: "Terminal 4",
        gate: "Gate G2",
        baggageCabin: "7 kg",
        baggageCheckIn: "20 kg"
    },
    {
        id: "FL-111",
        airlineName: "StarLink Aviation",
        airlineCode: "SL",
        flightNumber: "SL-678",
        logoColor: "#10b981",
        fromCity: "Dubai",
        fromCode: "DXB",
        toCity: "London",
        toCode: "LHR",
        depTime: "02:40 PM",
        arrTime: "07:15 PM",
        duration: "7h 35m",
        stops: 1,
        price: 410,
        seatsAvailable: 6,
        mealAvailable: true,
        wifiAvailable: true,
        aircraftType: "Airbus A380-800",
        terminal: "Terminal 3",
        gate: "Gate A3",
        baggageCabin: "10 kg",
        baggageCheckIn: "32 kg"
    },
    {
        id: "FL-112",
        airlineName: "JetStream Express",
        airlineCode: "JS",
        flightNumber: "JS-499",
        logoColor: "#06b6d4",
        fromCity: "London",
        fromCode: "LHR",
        toCity: "Dubai",
        toCode: "DXB",
        depTime: "10:30 PM",
        arrTime: "08:30 AM",
        duration: "7h 00m",
        stops: 0,
        price: 399,
        seatsAvailable: 10,
        mealAvailable: true,
        wifiAvailable: true,
        aircraftType: "Airbus A350-900",
        terminal: "Terminal 5",
        gate: "Gate C52",
        baggageCabin: "7 kg",
        baggageCheckIn: "30 kg"
    }
];

// APP CONSTANTS & COUPONS
const PROMO_CODES = {
    "EARLY10": 0.10, // 10% discount
    "FESTIVAL15": 0.15, // 15% discount
    "STUDENT20": 0.20, // 20% discount
    "CARD8": 0.08 // 8% card discount
};

const TRAVEL_CLASS_MULTIPLIERS = {
    "economy": 1.0,
    "premium-economy": 1.25,
    "business": 1.75,
    "first-class": 2.5
};

// GLOBAL DOM LOAD EVENT
document.addEventListener("DOMContentLoaded", () => {
    initTheme();
    initGlobalUI();
    
    // Page router logic
    const path = window.location.pathname.toLowerCase();
    
    if (path.endsWith("index.html") || path === "/" || path === "/flight-booking/") {
        initHomePage();
    } else if (path.endsWith("flights.html")) {
        initFlightsPage();
    } else if (path.endsWith("seat-selection.html")) {
        initSeatSelectionPage();
    } else if (path.endsWith("booking.html")) {
        initBookingPage();
    } else if (path.endsWith("offers.html")) {
        initOffersPage();
    } else if (path.endsWith("my-bookings.html")) {
        initMyBookingsPage();
    } else if (path.endsWith("about.html")) {
        initAboutPage();
    } else if (path.endsWith("contact.html")) {
        initContactPage();
    }
});

/* ==========================================================================
   GLOBAL THEME & INTERFACE CONTROLLERS
   ========================================================================== */
function initTheme() {
    const savedTheme = localStorage.getItem("theme") || "light";
    document.documentElement.setAttribute("data-theme", savedTheme);
    
    // Update theme toggle icons if present
    updateThemeToggleIcons(savedTheme);
}

function updateThemeToggleIcons(theme) {
    const themeBtn = document.getElementById("theme-toggle-btn");
    if (themeBtn) {
        const icon = themeBtn.querySelector("i");
        if (icon) {
            if (theme === "dark") {
                icon.className = "fas fa-sun";
            } else {
                icon.className = "fas fa-moon";
            }
        }
    }
}

function toggleTheme() {
    let currentTheme = document.documentElement.getAttribute("data-theme");
    let nextTheme = currentTheme === "dark" ? "light" : "dark";
    
    document.documentElement.setAttribute("data-theme", nextTheme);
    localStorage.setItem("theme", nextTheme);
    updateThemeToggleIcons(nextTheme);
    showToast(`Switched to ${nextTheme} theme`, "success");
}

function initGlobalUI() {
    // Theme Toggle click handler
    const themeBtn = document.getElementById("theme-toggle-btn");
    if (themeBtn) {
        themeBtn.addEventListener("click", toggleTheme);
    }
    
    // Hamburger menu toggle
    const hamburger = document.getElementById("hamburger-btn");
    const navMenu = document.getElementById("nav-menu");
    if (hamburger && navMenu) {
        hamburger.addEventListener("click", () => {
            hamburger.classList.toggle("active");
            navMenu.classList.toggle("active");
        });
    }

    // Scroll to top button
    const backToTop = document.getElementById("back-to-top-btn");
    if (backToTop) {
        window.addEventListener("scroll", () => {
            if (window.scrollY > 400) {
                backToTop.classList.add("active");
            } else {
                backToTop.classList.remove("active");
            }
        });
        backToTop.addEventListener("click", () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // Remove spinner loading screen after standard delay (simulating fetching assets)
    const loader = document.getElementById("global-loader");
    if (loader) {
        setTimeout(() => {
            loader.style.opacity = '0';
            setTimeout(() => {
                loader.style.display = 'none';
            }, 500);
        }, 300);
    }
}

/* ==========================================================================
   TOAST NOTIFICATION UTILITY
   ========================================================================== */
function showToast(message, type = "success") {
    let container = document.getElementById("toast-holder");
    if (!container) {
        container = document.createElement("div");
        container.id = "toast-holder";
        container.className = "toast-container";
        document.body.appendChild(container);
    }
    
    const toast = document.createElement("div");
    toast.className = `toast ${type}`;
    
    let iconClass = "fa-check-circle";
    if (type === "danger") iconClass = "fa-exclamation-circle";
    if (type === "warning") iconClass = "fa-info-circle";
    
    toast.innerHTML = `
        <i class="fas ${iconClass}" style="color: ${type === 'success' ? 'var(--success)' : type === 'danger' ? 'var(--danger)' : 'var(--warning)'}"></i>
        <div class="toast-message">${message}</div>
    `;
    
    container.appendChild(toast);
    
    setTimeout(() => {
        toast.style.animation = "slideInLeft 0.3s ease reverse";
        setTimeout(() => {
            toast.remove();
        }, 300);
    }, 3000);
}

/* ==========================================================================
   1. HOME PAGE CONTROLLER
   ========================================================================== */
function initHomePage() {
    const searchForm = document.getElementById("flight-search-form");
    if (searchForm) {
        searchForm.addEventListener("submit", (e) => {
            e.preventDefault();
            
            const fromAirport = document.getElementById("from-airport").value;
            const toAirport = document.getElementById("to-airport").value;
            const depDate = document.getElementById("dep-date").value;
            const retDate = document.getElementById("ret-date").value;
            const tripType = document.querySelector(".tab-btn.active").dataset.tripType;
            const passengers = document.getElementById("passenger-count").value;
            const travelClass = document.getElementById("travel-class").value;
            
            // VALIDATION
            if (!fromAirport || !toAirport) {
                showToast("Please specify both departure and arrival airports.", "danger");
                return;
            }
            if (fromAirport === toAirport) {
                showToast("Departure and arrival airports cannot be the same.", "danger");
                return;
            }
            if (!depDate) {
                showToast("Please select a departure date.", "danger");
                return;
            }
            
            const today = new Date().setHours(0,0,0,0);
            const selectedDep = new Date(depDate).setHours(0,0,0,0);
            if (selectedDep < today) {
                showToast("Departure date cannot be in the past.", "danger");
                return;
            }
            
            if (tripType === "round-trip" && !retDate) {
                showToast("Please select a return date for a round trip flight.", "danger");
                return;
            }
            if (tripType === "round-trip") {
                const selectedRet = new Date(retDate).setHours(0,0,0,0);
                if (selectedRet < selectedDep) {
                    showToast("Return date must be after departure date.", "danger");
                    return;
                }
            }

            // Save search to local storage
            const searchParams = {
                fromAirport,
                toAirport,
                depDate,
                retDate,
                tripType,
                passengers: parseInt(passengers) || 1,
                travelClass
            };
            localStorage.setItem("currentSearch", JSON.stringify(searchParams));

            // Save to recent searches array
            let recent = JSON.parse(localStorage.getItem("recentSearches")) || [];
            // Remove duplication
            recent = recent.filter(r => !(r.fromAirport === fromAirport && r.toAirport === toAirport));
            recent.unshift(searchParams);
            recent = recent.slice(0, 5); // limit to 5
            localStorage.setItem("recentSearches", JSON.stringify(recent));

            // Show loader animation simulation and redirect
            const loader = document.getElementById("global-loader");
            if (loader) {
                loader.style.display = "flex";
                loader.style.opacity = "1";
            }
            
            setTimeout(() => {
                window.location.href = "pages/flights.html";
            }, 800);
        });

        // Trip Type Tabs switcher
        const tabBtns = document.querySelectorAll(".search-tabs .tab-btn");
        const returnGroup = document.getElementById("ret-date-group");
        tabBtns.forEach(btn => {
            btn.addEventListener("click", () => {
                tabBtns.forEach(b => b.classList.remove("active"));
                btn.classList.add("active");
                
                if (btn.dataset.tripType === "round-trip") {
                    returnGroup.style.display = "flex";
                } else {
                    returnGroup.style.display = "none";
                }
            });
        });

        // Initialize form fields with today's dates
        const tomorrow = new Date();
        tomorrow.setDate(tomorrow.getDate() + 1);
        const depInput = document.getElementById("dep-date");
        const retInput = document.getElementById("ret-date");
        if (depInput) depInput.min = new Date().toISOString().split("T")[0];
        if (retInput) retInput.min = new Date().toISOString().split("T")[0];

        renderRecentSearches();
    }
}

function renderRecentSearches() {
    const holder = document.getElementById("recent-chips-holder");
    if (!holder) return;

    const recent = JSON.parse(localStorage.getItem("recentSearches")) || [];
    if (recent.length === 0) {
        holder.parentElement.style.display = "none";
        return;
    }

    holder.innerHTML = "";
    recent.forEach(search => {
        const chip = document.createElement("div");
        chip.className = "recent-chip animate-fade-in";
        chip.innerHTML = `<i class="fas fa-history"></i> ${search.fromAirport} ➔ ${search.toAirport} (${search.tripType === "round-trip" ? 'Round' : 'One Way'})`;
        chip.addEventListener("click", () => {
            document.getElementById("from-airport").value = search.fromAirport;
            document.getElementById("to-airport").value = search.toAirport;
            document.getElementById("dep-date").value = search.depDate;
            if (search.tripType === "round-trip") {
                const tabRound = document.querySelector(".tab-btn[data-trip-type='round-trip']");
                if (tabRound) tabRound.click();
                document.getElementById("ret-date").value = search.retDate;
            } else {
                const tabOne = document.querySelector(".tab-btn[data-trip-type='one-way']");
                if (tabOne) tabOne.click();
            }
            document.getElementById("passenger-count").value = search.passengers;
            document.getElementById("travel-class").value = search.travelClass;
            showToast("Pre-filled search criteria", "warning");
        });
        holder.appendChild(chip);
    });
}

/* ==========================================================================
   2. AVAILABLE FLIGHTS PAGE CONTROLLER
   ========================================================================== */
function initFlightsPage() {
    // Load current search parameters
    const searchData = JSON.parse(localStorage.getItem("currentSearch"));
    if (searchData) {
        const routeTitle = document.getElementById("flights-route-title");
        if (routeTitle) {
            routeTitle.textContent = `${searchData.fromAirport} ➔ ${searchData.toAirport}`;
        }
        const routeSubtitle = document.getElementById("flights-route-subtitle");
        if (routeSubtitle) {
            const depFmt = new Date(searchData.depDate).toLocaleDateString("en-US", { weekday: 'short', month: 'short', day: 'numeric' });
            const travellers = `${searchData.passengers} ${searchData.passengers > 1 ? 'Passengers' : 'Passenger'}`;
            const cls = searchData.travelClass.replace("-", " ").replace(/\b\w/g, c => c.toUpperCase());
            routeSubtitle.textContent = `${depFmt} | ${travellers} | ${cls}`;
        }
    }

    // Bind Filter inputs
    const filterPrice = document.getElementById("filter-price-range");
    if (filterPrice) {
        filterPrice.addEventListener("input", (e) => {
            const label = document.getElementById("filter-price-val");
            if (label) label.textContent = `$${e.target.value}`;
            renderFilteredFlights();
        });
    }

    const checkboxes = document.querySelectorAll(".sidebar-filter input[type='checkbox']");
    checkboxes.forEach(cb => {
        cb.addEventListener("change", renderFilteredFlights);
    });

    const sortBtns = document.querySelectorAll(".sort-options .sort-btn");
    sortBtns.forEach(btn => {
        btn.addEventListener("click", () => {
            sortBtns.forEach(b => b.classList.remove("active"));
            btn.classList.add("active");
            renderFilteredFlights();
        });
    });

    // Run first render
    renderFilteredFlights();
}

function renderFilteredFlights() {
    const listContainer = document.getElementById("flights-results-container");
    if (!listContainer) return;

    const searchData = JSON.parse(localStorage.getItem("currentSearch"));
    const fromAirport = searchData ? searchData.fromAirport.toLowerCase() : "";
    const toAirport = searchData ? searchData.toAirport.toLowerCase() : "";
    const travelClass = searchData ? searchData.travelClass : "economy";
    const classMultiplier = TRAVEL_CLASS_MULTIPLIERS[travelClass] || 1.0;

    // Filter Flights
    let filtered = MOCK_FLIGHTS.filter(flight => {
        // Source & Destination check (only if search parameters exist)
        if (fromAirport && toAirport) {
            const sourceMatches = flight.fromCode.toLowerCase() === fromAirport || flight.fromCity.toLowerCase().includes(fromAirport);
            const destMatches = flight.toCode.toLowerCase() === toAirport || flight.toCity.toLowerCase().includes(toAirport);
            if (!sourceMatches || !destMatches) return false;
        }

        // Price Filter
        const finalPrice = Math.round(flight.price * classMultiplier);
        const filterPriceVal = parseInt(document.getElementById("filter-price-range").value);
        if (finalPrice > filterPriceVal) return false;

        // Stops Filter
        const stopFilters = [];
        if (document.getElementById("stop-nonstop").checked) stopFilters.push(0);
        if (document.getElementById("stop-1stop").checked) stopFilters.push(1);
        if (document.getElementById("stop-2stop").checked) stopFilters.push(2);
        if (stopFilters.length > 0 && !stopFilters.includes(flight.stops)) return false;

        // Airlines Filter
        const airlineFilters = [];
        if (document.getElementById("air-horizon").checked) airlineFilters.push("horizon airways");
        if (document.getElementById("air-jetstream").checked) airlineFilters.push("jetstream express");
        if (document.getElementById("air-oceanic").checked) airlineFilters.push("oceanic air");
        if (document.getElementById("air-starlink").checked) airlineFilters.push("starlink aviation");
        if (airlineFilters.length > 0 && !airlineFilters.includes(flight.airlineName.toLowerCase())) return false;

        return true;
    });

    // Sorting
    const activeSort = document.querySelector(".sort-btn.active");
    if (activeSort) {
        const sortType = activeSort.dataset.sort;
        if (sortType === "price") {
            filtered.sort((a, b) => a.price - b.price);
        } else if (sortType === "duration") {
            const getMins = (dur) => {
                const parts = dur.split(" ");
                let total = 0;
                parts.forEach(p => {
                    if (p.endsWith("h")) total += parseInt(p) * 60;
                    if (p.endsWith("m")) total += parseInt(p);
                });
                return total;
            };
            filtered.sort((a, b) => getMins(a.duration) - getMins(b.duration));
        } else if (sortType === "stops") {
            filtered.sort((a, b) => a.stops - b.stops);
        }
    }

    // Render Cards
    listContainer.innerHTML = "";
    if (filtered.length === 0) {
        listContainer.innerHTML = `
            <div class="empty-bookings-state animate-fade-in">
                <i class="fas fa-plane-slash"></i>
                <h3>No Matching Flights Found</h3>
                <p>Try adjusting your search criteria, price range, or airlines filters.</p>
            </div>
        `;
        return;
    }

    // Load Favorites list
    const favs = JSON.parse(localStorage.getItem("favorites")) || [];

    filtered.forEach(flight => {
        const finalPrice = Math.round(flight.price * classMultiplier);
        const isFav = favs.includes(flight.id);
        const card = document.createElement("div");
        card.className = "flight-card animate-slide-up";
        card.innerHTML = `
            <button class="btn-icon favorite-btn" onclick="toggleFavorite('${flight.id}')">
                <i class="${isFav ? 'fas' : 'far'} fa-heart" style="color: ${isFav ? 'var(--danger)' : 'inherit'}"></i>
            </button>
            <div class="airline-info">
                <div class="airline-logo-svg" style="color: ${flight.logoColor}">
                    <i class="fas fa-plane"></i>
                </div>
                <div class="airline-details">
                    <h4>${flight.airlineName}</h4>
                    <span>${flight.flightNumber} • ${flight.aircraftType}</span>
                </div>
            </div>
            <div class="flight-timeline">
                <div class="time-node">
                    <h4>${flight.depTime}</h4>
                    <span>${flight.fromCode}</span>
                </div>
                <div class="timeline-path">
                    <div class="timeline-line"></div>
                    <i class="fas fa-plane timeline-plane"></i>
                    <div class="timeline-duration">${flight.duration}</div>
                    <div class="timeline-stops" style="font-size: 0.75rem; font-weight: 700; color: var(--text-muted)">
                        ${flight.stops === 0 ? 'Non-stop' : flight.stops === 1 ? '1 Stop' : `${flight.stops} Stops`}
                    </div>
                </div>
                <div class="time-node">
                    <h4>${flight.arrTime}</h4>
                    <span>${flight.toCode}</span>
                </div>
            </div>
            <div class="flight-pricing">
                <div class="price-display">$${finalPrice}</div>
                <div class="seats-remaining">${flight.seatsAvailable} seats left at this price</div>
                <button class="btn btn-primary" onclick="selectFlightForBooking('${flight.id}', ${finalPrice})">Book Now</button>
            </div>
        `;
        listContainer.appendChild(card);
    });
}

function selectFlightForBooking(flightId, finalPrice) {
    const flight = MOCK_FLIGHTS.find(f => f.id === flightId);
    if (!flight) return;

    const currentSearch = JSON.parse(localStorage.getItem("currentSearch")) || { passengers: 1, travelClass: "economy" };
    
    const bookingDetails = {
        flightId: flight.id,
        flightNumber: flight.flightNumber,
        airlineName: flight.airlineName,
        fromCode: flight.fromCode,
        fromCity: flight.fromCity,
        toCode: flight.toCode,
        toCity: flight.toCity,
        depTime: flight.depTime,
        arrTime: flight.arrTime,
        duration: flight.duration,
        priceUnit: finalPrice,
        passengersCount: currentSearch.passengers,
        travelClass: currentSearch.travelClass,
        selectedSeats: [],
        baseTotal: finalPrice * currentSearch.passengers,
        baggageAddon: 0,
        seatAddon: 0
    };

    localStorage.setItem("currentBooking", JSON.stringify(bookingDetails));
    window.location.href = "seat-selection.html";
}

function toggleFavorite(flightId) {
    let favs = JSON.parse(localStorage.getItem("favorites")) || [];
    if (favs.includes(flightId)) {
        favs = favs.filter(id => id !== flightId);
        showToast("Removed from favorite flights", "warning");
    } else {
        favs.push(flightId);
        showToast("Added to favorite flights", "success");
    }
    localStorage.setItem("favorites", JSON.stringify(favs));
    renderFilteredFlights();
}

/* ==========================================================================
   3. SEAT SELECTION CONTROLLER
   ========================================================================== */
function initSeatSelectionPage() {
    const booking = JSON.parse(localStorage.getItem("currentBooking"));
    if (!booking) {
        showToast("No active booking. Please select a flight first.", "danger");
        setTimeout(() => {
            window.location.href = "flights.html";
        }, 1500);
        return;
    }

    // Set header info
    document.getElementById("seat-route").textContent = `${booking.fromCode} ➔ ${booking.toCode}`;
    document.getElementById("seat-flight-info").textContent = `${booking.airlineName} • ${booking.flightNumber}`;
    document.getElementById("seat-pax-needed").textContent = booking.passengersCount;

    // Render Cabin Layout
    renderCabinGrid(booking);

    // Update Initial Pricing UI
    updateSeatSummaryPrice(booking);

    // Confirm Seats click
    const confirmBtn = document.getElementById("confirm-seats-btn");
    if (confirmBtn) {
        confirmBtn.addEventListener("click", () => {
            const updatedBooking = JSON.parse(localStorage.getItem("currentBooking"));
            if (updatedBooking.selectedSeats.length !== updatedBooking.passengersCount) {
                showToast(`Please select exactly ${updatedBooking.passengersCount} seats.`, "danger");
                return;
            }
            window.location.href = "booking.html";
        });
    }
}

function renderCabinGrid(booking) {
    const grid = document.getElementById("seat-cabin-grid");
    if (!grid) return;

    grid.innerHTML = "";

    // Columns: A, B, C, (Aisle), D, E, F
    // Rows: 1 to 10
    // Exit Row: Row 5
    // Random Mock Reserved Seats: 1C, 2A, 3F, 4D, 6E, 8A, 9B, 10F
    const reservedList = ["1C", "2A", "3F", "4D", "6E", "8A", "9B", "10F"];

    for (let row = 1; row <= 10; row++) {
        // Seat labels map
        const seatLetters = ["A", "B", "C", "Aisle", "D", "E", "F"];
        
        seatLetters.forEach((letter) => {
            if (letter === "Aisle") {
                const aisleDiv = document.createElement("div");
                aisleDiv.className = "seat aisle";
                aisleDiv.textContent = row;
                grid.appendChild(aisleDiv);
            } else {
                const seatId = `${row}${letter}`;
                const seatDiv = document.createElement("div");
                
                let isExit = (row === 5);
                let isReserved = reservedList.includes(seatId);
                let isSelected = booking.selectedSeats.includes(seatId);

                let className = "seat";
                if (isExit) className += " exit-row";
                if (isReserved) className += " reserved";
                if (isSelected) className += " selected";

                seatDiv.className = className;
                seatDiv.textContent = seatId;
                
                if (!isReserved) {
                    seatDiv.addEventListener("click", () => {
                        toggleSeatSelection(seatId, isExit);
                    });
                }
                grid.appendChild(seatDiv);
            }
        });
    }
}

function toggleSeatSelection(seatId, isExit) {
    const booking = JSON.parse(localStorage.getItem("currentBooking"));
    let seats = booking.selectedSeats;

    if (seats.includes(seatId)) {
        // Deselect
        seats = seats.filter(s => s !== seatId);
        showToast(`Seat ${seatId} deselected`, "warning");
    } else {
        // Select
        if (seats.length >= booking.passengersCount) {
            // Remove first, FIFO
            const removed = seats.shift();
            // Need to update class of that removed seat on UI
            const seatElements = document.querySelectorAll(".seat");
            seatElements.forEach(s => {
                if (s.textContent === removed) {
                    s.classList.remove("selected");
                }
            });
        }
        seats.push(seatId);
        showToast(`Seat ${seatId} selected!`, "success");
    }

    booking.selectedSeats = seats;
    
    // Calculate seat surcharge: $25 for normal, $50 for exit row premium
    let seatCharge = 0;
    seats.forEach(s => {
        const row = parseInt(s);
        if (row === 5) {
            seatCharge += 50; // Exit row premium
        } else {
            seatCharge += 20; // Standard selection charge
        }
    });

    booking.seatAddon = seatCharge;
    localStorage.setItem("currentBooking", JSON.stringify(booking));

    // Update visually
    const seatElements = document.querySelectorAll(".seat");
    seatElements.forEach(s => {
        if (s.textContent === seatId) {
            s.classList.toggle("selected");
        }
    });

    updateSeatSummaryPrice(booking);
}

function updateSeatSummaryPrice(booking) {
    const countSpan = document.getElementById("selected-seats-count");
    const listSpan = document.getElementById("selected-seats-list");
    const baseSpan = document.getElementById("summary-base-price");
    const surchargeSpan = document.getElementById("summary-seat-surcharge");
    const totalSpan = document.getElementById("summary-grand-total");

    if (countSpan) countSpan.textContent = booking.selectedSeats.length;
    if (listSpan) listSpan.textContent = booking.selectedSeats.length > 0 ? booking.selectedSeats.join(", ") : "None";
    if (baseSpan) baseSpan.textContent = `$${booking.baseTotal}`;
    if (surchargeSpan) surchargeSpan.textContent = `$${booking.seatAddon}`;
    if (totalSpan) totalSpan.textContent = `$${booking.baseTotal + booking.seatAddon}`;
}

/* ==========================================================================
   4. PASSENGER DETAILS & BOOKING FORM CONTROLLER
   ========================================================================== */
function initBookingPage() {
    const booking = JSON.parse(localStorage.getItem("currentBooking"));
    if (!booking) {
        showToast("No active booking session.", "danger");
        setTimeout(() => { window.location.href = "flights.html"; }, 1500);
        return;
    }

    // Dynamic passenger input generation
    const formsHolder = document.getElementById("passenger-forms-container");
    if (formsHolder) {
        formsHolder.innerHTML = "";
        for (let i = 1; i <= booking.passengersCount; i++) {
            const formSection = document.createElement("div");
            formSection.className = "passenger-form-section animate-slide-up";
            formSection.style.marginBottom = "30px";
            formSection.innerHTML = `
                <h3 style="margin-bottom: 20px; border-bottom: 1px solid var(--border-color); padding-bottom: 8px;">
                    <i class="fas fa-user-circle"></i> Passenger #${i} ${i === 1 ? '(Primary Contact)' : ''}
                </h3>
                <div class="passenger-grid">
                    <div class="form-group">
                        <label>Full Name *</label>
                        <input type="text" class="form-input pax-name" required placeholder="John Doe">
                    </div>
                    <div class="form-group">
                        <label>Passport Number *</label>
                        <input type="text" class="form-input pax-passport" required placeholder="A1234567">
                    </div>
                    <div class="form-group">
                        <label>Nationality *</label>
                        <input type="text" class="form-input pax-nation" required placeholder="United States">
                    </div>
                    <div class="form-group">
                        <label>Date of Birth *</label>
                        <input type="date" class="form-input pax-dob" required>
                    </div>
                </div>
            `;
            formsHolder.appendChild(formSection);
        }
    }

    // Pre-populate summary cards
    const summaryDest = document.getElementById("booking-summary-route");
    const summaryDetails = document.getElementById("booking-summary-flight");
    const summarySeats = document.getElementById("booking-summary-seats");

    if (summaryDest) summaryDest.textContent = `${booking.fromCode} ➔ ${booking.toCode}`;
    if (summaryDetails) summaryDetails.textContent = `${booking.airlineName} • ${booking.flightNumber}`;
    if (summarySeats) summarySeats.textContent = booking.selectedSeats.join(", ");

    // Handle baggage addon checkbox click
    const baggageCheckbox = document.getElementById("baggage-addon-checkbox");
    if (baggageCheckbox) {
        baggageCheckbox.addEventListener("change", (e) => {
            const details = JSON.parse(localStorage.getItem("currentBooking"));
            details.baggageAddon = e.target.checked ? (45 * details.passengersCount) : 0;
            localStorage.setItem("currentBooking", JSON.stringify(details));
            updateFareBreakdown(details);
        });
    }

    // Apply Promo Code
    const applyPromoBtn = document.getElementById("apply-promo-btn");
    if (applyPromoBtn) {
        applyPromoBtn.addEventListener("click", () => {
            const promoInput = document.getElementById("promo-code-input").value.trim().toUpperCase();
            const details = JSON.parse(localStorage.getItem("currentBooking"));
            
            if (PROMO_CODES[promoInput]) {
                const rate = PROMO_CODES[promoInput];
                details.discountAmount = Math.round(details.baseTotal * rate);
                details.appliedPromo = promoInput;
                localStorage.setItem("currentBooking", JSON.stringify(details));
                showToast(`Promo applied successfully! ${rate * 100}% off base fare.`, "success");
                updateFareBreakdown(details);
            } else {
                showToast("Invalid Promo Code", "danger");
            }
        });
    }

    // Update initially
    updateFareBreakdown(booking);

    // Book & Pay form submit
    const finalForm = document.getElementById("final-booking-form");
    if (finalForm) {
        finalForm.addEventListener("submit", (e) => {
            e.preventDefault();

            // Contact Form validation
            const phone = document.getElementById("contact-phone").value.trim();
            const email = document.getElementById("contact-email").value.trim();

            if (!/^\+?\d{10,14}$/.test(phone)) {
                showToast("Please enter a valid phone number (10 to 14 digits).", "danger");
                return;
            }

            if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
                showToast("Please enter a valid email address.", "danger");
                return;
            }

            // Collect passengers name for boarding passes
            const nameInputs = document.querySelectorAll(".pax-name");
            const passportInputs = document.querySelectorAll(".pax-passport");
            
            const passengers = [];
            nameInputs.forEach((inp, idx) => {
                passengers.push({
                    name: inp.value.trim(),
                    passport: passportInputs[idx].value.trim(),
                    seat: booking.selectedSeats[idx]
                });
            });

            // Simulate credit card loading screen
            const loader = document.getElementById("global-loader");
            if (loader) {
                loader.style.display = "flex";
                loader.style.opacity = "1";
                const loaderText = loader.querySelector(".loader-text");
                if (loaderText) loaderText.textContent = "Processing Payment...";
            }

            setTimeout(() => {
                if (loader) {
                    loader.style.opacity = "0";
                    setTimeout(() => { loader.style.display = "none"; }, 500);
                }

                // Generate booking confirmation
                const bookingId = "BK-" + Math.floor(100000 + Math.random() * 900000);
                const currentBooking = JSON.parse(localStorage.getItem("currentBooking"));
                const totalCalculated = currentBooking.baseTotal + currentBooking.seatAddon + (50 * currentBooking.passengersCount) + currentBooking.baggageAddon - (currentBooking.discountAmount || 0);

                const finalRecord = {
                    bookingId,
                    flightNumber: currentBooking.flightNumber,
                    airlineName: currentBooking.airlineName,
                    fromCode: currentBooking.fromCode,
                    fromCity: currentBooking.fromCity,
                    toCode: currentBooking.toCode,
                    toCity: currentBooking.toCity,
                    depTime: currentBooking.depTime,
                    arrTime: currentBooking.arrTime,
                    duration: currentBooking.duration,
                    passengers,
                    totalPaid: totalCalculated,
                    bookingDate: new Date().toLocaleDateString(),
                    status: "Confirmed"
                };

                // Save to bookings list in localStorage
                const allBookings = JSON.parse(localStorage.getItem("bookings")) || [];
                allBookings.push(finalRecord);
                localStorage.setItem("bookings", JSON.stringify(allBookings));

                // Open modal
                openBookingSuccessModal(finalRecord);

                // Clear currentBooking session
                localStorage.removeItem("currentBooking");
            }, 1800);
        });
    }
}

function updateFareBreakdown(booking) {
    const baseSpan = document.getElementById("fare-base");
    const seatSpan = document.getElementById("fare-seats");
    const taxSpan = document.getElementById("fare-taxes");
    const luggageSpan = document.getElementById("fare-luggage");
    const promoRow = document.getElementById("fare-promo-row");
    const promoSpan = document.getElementById("fare-promo-discount");
    const grandSpan = document.getElementById("fare-grand-total");

    const taxAmount = 50 * booking.passengersCount; // Flat $50 tax per passenger
    const discount = booking.discountAmount || 0;
    const finalTotal = booking.baseTotal + booking.seatAddon + taxAmount + booking.baggageAddon - discount;

    if (baseSpan) baseSpan.textContent = `$${booking.baseTotal}`;
    if (seatSpan) seatSpan.textContent = `$${booking.seatAddon}`;
    if (taxSpan) taxSpan.textContent = `$${taxAmount}`;
    if (luggageSpan) luggageSpan.textContent = `$${booking.baggageAddon}`;
    
    if (discount > 0) {
        if (promoRow) promoRow.style.display = "flex";
        if (promoSpan) promoSpan.textContent = `-$${discount}`;
    } else {
        if (promoRow) promoRow.style.display = "none";
    }

    if (grandSpan) grandSpan.textContent = `$${finalTotal}`;
}

function openBookingSuccessModal(record) {
    const modal = document.getElementById("success-modal-overlay");
    if (!modal) return;

    modal.classList.add("active");
    
    // Fill dynamic confirmation details
    document.getElementById("modal-booking-id").textContent = record.bookingId;
    document.getElementById("modal-pax-primary").textContent = record.passengers[0].name;
    document.getElementById("modal-flight-code").textContent = `${record.airlineName} ${record.flightNumber}`;
    document.getElementById("modal-route").textContent = `${record.fromCity} (${record.fromCode}) to ${record.toCity} (${record.toCode})`;
    document.getElementById("modal-seats").textContent = record.passengers.map(p => p.seat).join(", ");
    document.getElementById("modal-amount").textContent = `$${record.totalPaid}`;
}

/* ==========================================================================
   5. OFFERS CONTROLLER & TIMER
   ========================================================================== */
function initOffersPage() {
    // Setup dynamic countdown timers for coupons
    const countdowns = document.querySelectorAll(".offer-timer span");
    if (countdowns.length > 0) {
        // Set target countdown date to 10 hours from now
        let countdownSecs = 10 * 3600 + 45 * 60; // 10h 45m
        
        const updateTimer = () => {
            if (countdownSecs <= 0) {
                countdowns.forEach(el => el.textContent = "EXPIRED");
                clearInterval(interval);
                return;
            }
            countdownSecs--;
            const hrs = Math.floor(countdownSecs / 3600);
            const mins = Math.floor((countdownSecs % 3600) / 60);
            const secs = countdownSecs % 60;
            
            const timeStr = `${hrs.toString().padStart(2, '0')}h ${mins.toString().padStart(2, '0')}m ${secs.toString().padStart(2, '0')}s`;
            countdowns.forEach(el => {
                el.textContent = timeStr;
            });
        };
        
        const interval = setInterval(updateTimer, 1000);
        updateTimer();
    }
}

// Clipboard copying utility
function copyPromoCode(code) {
    navigator.clipboard.writeText(code).then(() => {
        showToast(`Promo Code ${code} copied to clipboard!`, "success");
    }).catch(err => {
        showToast("Failed to copy promo code", "danger");
    });
}

/* ==========================================================================
   6. MY BOOKINGS HISTORY CONTROLLER
   ========================================================================== */
function initMyBookingsPage() {
    renderBookingsList();
}

function renderBookingsList() {
    const container = document.getElementById("my-bookings-container");
    if (!container) return;

    const bookings = JSON.parse(localStorage.getItem("bookings")) || [];
    
    if (bookings.length === 0) {
        container.innerHTML = `
            <div class="empty-bookings-state animate-fade-in">
                <i class="fas fa-ticket-alt"></i>
                <h3>No Bookings Found</h3>
                <p>You haven't made any flight reservations yet. Go search flights to book your next trip!</p>
                <a href="../index.html" class="btn btn-primary" style="margin-top: 24px;">Search Flights</a>
            </div>
        `;
        return;
    }

    container.innerHTML = "";
    bookings.forEach(rec => {
        const passCard = document.createElement("div");
        passCard.className = "bookings-record-card animate-slide-up";
        passCard.style.marginBottom = "40px";
        
        let passengersHtml = "";
        rec.passengers.forEach(p => {
            passengersHtml += `
                <div class="bp-row">
                    <div class="bp-field">
                        <label>Passenger Name</label>
                        <span>${p.name}</span>
                    </div>
                    <div class="bp-field">
                        <label>Passport</label>
                        <span>${p.passport}</span>
                    </div>
                    <div class="bp-field">
                        <label>Seat Number</label>
                        <span>${p.seat}</span>
                    </div>
                </div>
            `;
        });

        passCard.innerHTML = `
            <div class="boarding-pass">
                <div class="bp-header">
                    <div style="font-weight: 800; font-size: 1.25rem;">
                        <i class="fas fa-plane"></i> SKYPASS BOARDING DOCUMENT
                    </div>
                    <div style="font-weight: 700; font-family: monospace; font-size: 1.1rem;">
                        BOOKING ID: ${rec.bookingId}
                    </div>
                </div>
                <div class="bp-body">
                    <div class="bp-row">
                        <div class="bp-field">
                            <label>From</label>
                            <span>${rec.fromCity} (${rec.fromCode})</span>
                        </div>
                        <div class="bp-field">
                            <label>To</label>
                            <span>${rec.toCity} (${rec.toCode})</span>
                        </div>
                        <div class="bp-field">
                            <label>Airline / Flight</label>
                            <span>${rec.airlineName} (${rec.flightNumber})</span>
                        </div>
                    </div>
                    
                    <div class="bp-row">
                        <div class="bp-field">
                            <label>Departure Time</label>
                            <span>${rec.depTime}</span>
                        </div>
                        <div class="bp-field">
                            <label>Arrival Time</label>
                            <span>${rec.arrTime}</span>
                        </div>
                        <div class="bp-field">
                            <label>Status</label>
                            <span style="color: ${rec.status === 'Confirmed' ? 'var(--success)' : 'var(--danger)'}">
                                ${rec.status}
                            </span>
                        </div>
                    </div>

                    <div style="border-top: 1px solid var(--border-color); padding-top: 20px; margin-top: 20px;">
                        <h4 style="font-size: 0.9rem; text-transform: uppercase; color: var(--text-muted); margin-bottom: 16px;">Passenger Seats Details</h4>
                        ${passengersHtml}
                    </div>

                    <div class="bp-barcode-container">
                        <div class="bp-barcode"></div>
                        <div style="font-size: 0.8rem; font-weight: 600; color: var(--text-secondary); letter-spacing: 2px;">
                            ${rec.bookingId}-${rec.flightNumber}
                        </div>
                    </div>

                    <div style="margin-top: 24px; display: flex; justify-content: flex-end; gap: 12px;">
                        ${rec.status === 'Confirmed' ? `
                            <button class="btn btn-outline" onclick="cancelBooking('${rec.bookingId}')" style="border-color: var(--danger); color: var(--danger)">
                                <i class="fas fa-trash-alt"></i> Cancel Reservation
                            </button>
                        ` : ''}
                        <button class="btn btn-primary" onclick="window.print()">
                            <i class="fas fa-print"></i> Print Ticket
                        </button>
                    </div>
                </div>
            </div>
        `;
        container.appendChild(passCard);
    });
}

function cancelBooking(bookingId) {
    if (!confirm("Are you sure you want to cancel this flight reservation? This action cannot be undone.")) {
        return;
    }

    let bookings = JSON.parse(localStorage.getItem("bookings")) || [];
    bookings = bookings.map(b => {
        if (b.bookingId === bookingId) {
            b.status = "Cancelled";
        }
        return b;
    });

    localStorage.setItem("bookings", JSON.stringify(bookings));
    showToast(`Reservation ${bookingId} has been cancelled successfully.`, "danger");
    renderBookingsList();
}

/* ==========================================================================
   7. ABOUT PAGE & FAQ ACCORDION CONTROLLER
   ========================================================================== */
function initAboutPage() {
    const accordionHeaders = document.querySelectorAll(".accordion-header");
    accordionHeaders.forEach(header => {
        header.addEventListener("click", () => {
            const item = header.parentElement;
            const content = item.querySelector(".accordion-content");
            const isActive = item.classList.contains("active");

            // Close all items
            document.querySelectorAll(".accordion-item").forEach(itm => {
                itm.classList.remove("active");
                itm.querySelector(".accordion-content").style.maxHeight = null;
            });

            // Toggle selected item
            if (!isActive) {
                item.classList.add("active");
                content.style.maxHeight = content.scrollHeight + "px";
            }
        });
    });
}

/* ==========================================================================
   8. CONTACT PAGE CONTROLLER
   ========================================================================== */
function initContactPage() {
    const contactForm = document.getElementById("contact-us-form");
    if (contactForm) {
        contactForm.addEventListener("submit", (e) => {
            e.preventDefault();
            
            // Show toast message
            showToast("Your message was sent successfully. Customer support will contact you shortly.", "success");
            contactForm.reset();
        });
    }
}
