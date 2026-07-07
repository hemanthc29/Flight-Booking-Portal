from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path('process/<int:booking_id>/', views.process_payment_view, name='process_payment'),
    path('confirmation/<int:booking_id>/', views.payment_confirmation_view, name='confirmation'),
]
