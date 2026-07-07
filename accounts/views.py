from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import get_user_model

from .forms import UserRegisterForm, UserLoginForm, ProfileUpdateForm, PasswordResetRequestForm
from bookings.models import Booking

User = get_user_model()

def register_view(request):
    if request.user.is_authenticated:
        return redirect('flights:home')
        
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Welcome to Flight Booking, {user.first_name}! A confirmation link has been sent to {user.email}.")
            return redirect('accounts:verify_email')
    else:
        form = UserRegisterForm()
    return render(request, 'profile.html', {'form': form, 'auth_action': 'register'})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('flights:home')
        
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {user.username}!")
                # Check redirect target
                next_url = request.GET.get('next', 'flights:home')
                return redirect(next_url)
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid form submission.")
    else:
        form = UserLoginForm()
    return render(request, 'profile.html', {'form': form, 'auth_action': 'login'})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('flights:home')

@login_required
def profile_view(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated successfully!")
            return redirect('accounts:profile')
    else:
        form = ProfileUpdateForm(instance=user)
        
    bookings = Booking.objects.filter(user=user).order_on = '-booking_date'
    bookings = Booking.objects.filter(user=user).order_by('-booking_date')
    return render(request, 'profile.html', {
        'form': form,
        'bookings': bookings,
        'auth_action': 'profile'
    })

@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Keep the user logged in
            messages.success(request, 'Your password was successfully updated!')
            return redirect('accounts:profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'profile.html', {'form': form, 'auth_action': 'change_password'})

def verify_email_view(request):
    # Simulate verification
    if request.user.is_authenticated:
        user = request.user
        user.email_verified = True
        user.save()
    return render(request, 'profile.html', {'auth_action': 'verify_email'})

def reset_password_view(request):
    if request.method == 'POST':
        form = PasswordResetRequestForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            messages.success(request, f"A password reset link has been dispatched to {email}.")
            return redirect('accounts:login')
    else:
        form = PasswordResetRequestForm()
    return render(request, 'profile.html', {'form': form, 'auth_action': 'reset_password'})
