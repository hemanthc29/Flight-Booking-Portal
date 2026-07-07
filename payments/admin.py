from django.contrib import admin
from .models import Payment, Ticket

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'booking', 'payment_method', 'amount', 'payment_date', 'status')
    list_filter = ('status', 'payment_method')

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('ticket_number', 'booking', 'passenger', 'created_at')
