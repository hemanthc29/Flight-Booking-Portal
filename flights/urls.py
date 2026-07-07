from django.urls import path
from . import views

app_name = 'flights'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('search/', views.flight_search_view, name='search'),
    path('flight/<int:flight_id>/', views.flight_details_view, name='details'),
    path('flight/<int:flight_id>/add-review/', views.add_review_view, name='add_review'),
    path('review/edit/<int:review_id>/', views.edit_review_view, name='edit_review'),
    path('review/delete/<int:review_id>/', views.delete_review_view, name='delete_review'),
    path('wishlist/', views.wishlist_view, name='wishlist'),
    path('wishlist/sync/', views.wishlist_sync_view, name='wishlist_sync'),
    path('compare/', views.flight_compare_view, name='compare'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('faq/', views.faq_view, name='faq'),
    path('airports/', views.airports_view, name='airports'),
    path('airlines/', views.airlines_view, name='airlines'),
    path('offers/', views.offers_view, name='offers'),
    path('admin-dashboard/', views.admin_dashboard_view, name='admin_dashboard'),
    path('admin-dashboard/block-user/<int:user_id>/', views.admin_block_user_view, name='admin_block_user'),
    path('admin-dashboard/delete-user/<int:user_id>/', views.admin_delete_user_view, name='admin_delete_user'),
    path('admin-dashboard/refund-booking/<int:booking_id>/', views.admin_refund_booking_view, name='admin_refund_booking'),
    path('admin-dashboard/cancel-booking/<int:booking_id>/', views.admin_cancel_booking_view, name='admin_cancel_booking'),
    path('newsletter/subscribe/', views.newsletter_subscribe_view, name='newsletter_subscribe'),
]
