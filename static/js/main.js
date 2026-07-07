document.addEventListener('DOMContentLoaded', () => {
    // 1. Loading Screen Animation
    const loader = document.getElementById('loader-screen');
    if (loader) {
        window.addEventListener('load', () => {
            loader.style.opacity = '0';
            setTimeout(() => {
                loader.style.display = 'none';
            }, 500);
        });
        // Safety timeout
        setTimeout(() => {
            if (loader.style.display !== 'none') {
                loader.style.opacity = '0';
                setTimeout(() => {
                    loader.style.display = 'none';
                }, 500);
            }
        }, 2000);
    }

    // 2. Theme Toggle logic
    const themeToggleBtn = document.getElementById('theme-toggle-btn');
    if (themeToggleBtn) {
        const icon = themeToggleBtn.querySelector('i');
        
        // Function to update icon class based on theme
        const updateThemeIcon = (theme) => {
            if (theme === 'dark') {
                icon.className = 'fas fa-sun text-warning';
            } else {
                icon.className = 'fas fa-moon';
            }
        };

        // Initialize state
        const savedTheme = localStorage.getItem('theme') || 'light';
        updateThemeIcon(savedTheme);
        if (savedTheme === 'dark') {
            document.documentElement.classList.add('dark-theme');
            document.body.classList.add('dark-theme');
        }

        themeToggleBtn.addEventListener('click', () => {
            const isDark = document.documentElement.classList.contains('dark-theme');
            if (isDark) {
                document.documentElement.classList.remove('dark-theme');
                document.body.classList.remove('dark-theme');
                localStorage.setItem('theme', 'light');
                updateThemeIcon('light');
                showToast('Light theme activated!', 'success');
            } else {
                document.documentElement.classList.add('dark-theme');
                document.body.classList.add('dark-theme');
                localStorage.setItem('theme', 'dark');
                updateThemeIcon('dark');
                showToast('Dark theme activated!', 'success');
            }
        });
    }

    // 2b. Page Transitions & Link Interception
    const transitionOverlay = document.getElementById('page-transition-overlay');
    if (transitionOverlay) {
        // Fade out overlay on page load
        setTimeout(() => {
            transitionOverlay.style.opacity = '0';
        }, 50);

        // Intercept internal link clicks
        document.querySelectorAll('a').forEach(link => {
            const href = link.getAttribute('href');
            
            // Only intercept local relative or absolute origin links
            if (href && 
                !href.startsWith('#') && 
                !href.startsWith('javascript:') && 
                !href.startsWith('mailto:') && 
                !href.startsWith('tel:') && 
                !link.getAttribute('target') && 
                !href.includes('logout') && 
                !href.includes('admin') && 
                !link.classList.contains('dropdown-toggle') &&
                !link.classList.contains('no-transition')) {
                
                // Ensure same host (either relative path or absolute matching hostname)
                const isInternal = href.startsWith('/') || href.startsWith(window.location.origin) || !href.includes('://');
                if (isInternal) {
                    link.addEventListener('click', (e) => {
                        e.preventDefault();
                        transitionOverlay.classList.add('active');
                        setTimeout(() => {
                            window.location.href = href;
                        }, 400);
                    });
                }
            }
        });
    }

    // 3. Back to Top Button
    const backToTopBtn = document.getElementById('btn-back-to-top');
    if (backToTopBtn) {
        window.addEventListener('scroll', () => {
            if (document.body.scrollTop > 300 || document.documentElement.scrollTop > 300) {
                backToTopBtn.style.display = 'block';
            } else {
                backToTopBtn.style.display = 'none';
            }
        });
        backToTopBtn.addEventListener('click', () => {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // 4. Toast Notifications
    window.showToast = function(message, type = 'success') {
        const container = document.getElementById('toast-container');
        if (!container) return;
        
        const toast = document.createElement('div');
        toast.className = `custom-toast ${type}`;
        
        let iconClass = 'fa-check-circle';
        if (type === 'error') iconClass = 'fa-exclamation-circle';
        
        toast.innerHTML = `
            <div class="custom-toast-icon"><i class="fas ${iconClass}"></i></div>
            <div class="custom-toast-message">${message}</div>
        `;
        
        container.appendChild(toast);
        
        // Trigger animation
        setTimeout(() => toast.classList.add('show'), 50);
        
        // Remove toast
        setTimeout(() => {
            toast.classList.remove('show');
            setTimeout(() => toast.remove(), 400);
        }, 3000);
    };

    // 5. Scroll Animations Trigger (Fade-in, Zoom, Slide)
    const animElements = document.querySelectorAll('.animate-on-scroll');
    if (animElements.length > 0) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const animType = entry.target.getAttribute('data-animation') || 'fade-in-up';
                    entry.target.classList.add(animType);
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1 });
        
        animElements.forEach(el => observer.observe(el));
    }

    // 6. Date Validations (Prevent Past dates, invalid return dates)
    const departureInput = document.getElementById('departure_date');
    const returnInput = document.getElementById('return_date');
    if (departureInput) {
        const today = new Date().toISOString().split('T')[0];
        departureInput.setAttribute('min', today);
        
        departureInput.addEventListener('change', () => {
            if (returnInput) {
                returnInput.setAttribute('min', departureInput.value);
                if (returnInput.value && returnInput.value < departureInput.value) {
                    returnInput.value = departureInput.value;
                }
            }
        });
    }
    if (returnInput) {
        const today = new Date().toISOString().split('T')[0];
        returnInput.setAttribute('min', today);
    }

    // 7. Local Storage Wishlist & Synced Backend
    window.toggleWishlist = function(flightId, buttonElement) {
        let wishlist = JSON.parse(localStorage.getItem('wishlist') || '[]');
        const idx = wishlist.indexOf(flightId);
        
        if (idx > -1) {
            wishlist.splice(idx, 1);
            localStorage.setItem('wishlist', JSON.stringify(wishlist));
            if (buttonElement) {
                buttonElement.innerHTML = '<i class="far fa-heart"></i>';
                buttonElement.classList.remove('active');
            }
            showToast('Flight removed from wishlist!', 'success');
            syncWishlistBackend(flightId, 'remove');
        } else {
            wishlist.push(flightId);
            localStorage.setItem('wishlist', JSON.stringify(wishlist));
            if (buttonElement) {
                buttonElement.innerHTML = '<i class="fas fa-heart text-danger"></i>';
                buttonElement.classList.add('active');
            }
            showToast('Flight added to wishlist!', 'success');
            syncWishlistBackend(flightId, 'add');
        }
    };

    function syncWishlistBackend(flightId, action) {
        // Quietly attempt to sync if user is logged in
        fetch('/flights/wishlist/sync/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({ flight_id: flightId, action: action })
        }).catch(err => console.log('Wishlist sync bypassed or unauthenticated:', err));
    }

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // Check wishlist items on page load to color hearts
    const wishlistBtns = document.querySelectorAll('.wishlist-toggle-btn');
    if (wishlistBtns.length > 0) {
        let wishlist = JSON.parse(localStorage.getItem('wishlist') || '[]');
        wishlistBtns.forEach(btn => {
            const flightId = btn.getAttribute('data-flight-id');
            if (wishlist.includes(flightId)) {
                btn.innerHTML = '<i class="fas fa-heart text-danger"></i>';
                btn.classList.add('active');
            }
        });
    }

    // 8. Flight Comparison Panel Logic
    const compareCheckboxes = document.querySelectorAll('.compare-checkbox');
    const compareWidget = document.getElementById('compare-widget');
    const compareList = document.getElementById('compare-list');
    const compareButton = document.getElementById('btn-compare-action');
    let comparedFlights = [];

    if (compareCheckboxes.length > 0 && compareWidget) {
        compareCheckboxes.forEach(checkbox => {
            checkbox.addEventListener('change', (e) => {
                const flightId = e.target.getAttribute('data-flight-id');
                const flightNum = e.target.getAttribute('data-flight-num');
                const airline = e.target.getAttribute('data-airline');
                const fare = e.target.getAttribute('data-fare');
                
                if (e.target.checked) {
                    if (comparedFlights.length >= 3) {
                        e.target.checked = false;
                        showToast('You can compare a maximum of 3 flights at once.', 'error');
                        return;
                    }
                    comparedFlights.push({ id: flightId, num: flightNum, airline: airline, fare: fare });
                } else {
                    comparedFlights = comparedFlights.filter(f => f.id !== flightId);
                }
                
                updateCompareWidget();
            });
        });
    }

    function updateCompareWidget() {
        if (comparedFlights.length > 0) {
            compareWidget.classList.add('show');
            compareList.innerHTML = comparedFlights.map(f => `
                <div class="badge bg-primary p-2 me-2 mb-1 d-inline-flex align-items-center">
                    <span>${f.airline} (${f.num}) - $${f.fare}</span>
                    <button type="button" class="btn-close btn-close-white ms-2" style="font-size:0.6rem;" onclick="removeComparedFlight('${f.id}')"></button>
                </div>
            `).join('');
            
            if (comparedFlights.length >= 2) {
                compareButton.removeAttribute('disabled');
            } else {
                compareButton.setAttribute('disabled', 'true');
            }
        } else {
            compareWidget.classList.remove('show');
        }
    }

    window.removeComparedFlight = function(flightId) {
        comparedFlights = comparedFlights.filter(f => f.id !== flightId);
        const checkbox = document.querySelector(`.compare-checkbox[data-flight-id="${flightId}"]`);
        if (checkbox) checkbox.checked = false;
        updateCompareWidget();
    };

    if (compareButton) {
        compareButton.addEventListener('click', () => {
            const ids = comparedFlights.map(f => f.id).join(',');
            window.location.href = `/flights/compare/?ids=${ids}`;
        });
    }
});
