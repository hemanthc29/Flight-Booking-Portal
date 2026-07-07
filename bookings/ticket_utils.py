import os
import qrcode
import io
from io import BytesIO
from django.core.files.base import ContentFile
from django.conf import settings
from django.core.files import File

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

from payments.models import Ticket

def generate_ticket_assets(booking, passenger):
    """
    Generates a unique Ticket record, drawing a QR code and compiling 
    a styled PDF boarding pass for the passenger using ReportLab.
    """
    ticket_num = f"TKT-{booking.pnr}-{passenger.id}"
    
    # 1. Generate QR Code
    qr_data = f"Ticket: {ticket_num}\nPNR: {booking.pnr}\nFlight: {booking.flight.flight_number}\nPassenger: {passenger.first_name} {passenger.last_name}\nSeat: {passenger.seat.seat_number if passenger.seat else 'N/A'}"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=4,
        border=1,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)
    
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_buffer = BytesIO()
    qr_img.save(qr_buffer, format="PNG")
    qr_buffer.seek(0)
    
    # Create the Ticket record (without files first)
    ticket, created = Ticket.objects.get_or_create(
        booking=booking,
        passenger=passenger,
        defaults={'ticket_number': ticket_num}
    )
    
    # Save the QR code image file
    qr_filename = f"qr_{ticket_num}.png"
    ticket.qr_code.save(qr_filename, File(qr_buffer), save=False)
    
    # 2. Generate PDF using ReportLab
    pdf_buffer = BytesIO()
    p = canvas.Canvas(pdf_buffer, pagesize=letter)
    width, height = letter
    
    # Draw ticket layout
    # Main Indigo header bar
    p.setFillColor(HexColor("#6366f1"))
    p.rect(36, height - 120, width - 72, 80, fill=True, stroke=False)
    
    # Header Text
    p.setFillColor(HexColor("#ffffff"))
    p.setFont("Helvetica-Bold", 24)
    p.drawString(56, height - 80, "BOARDING PASS / E-TICKET")
    
    p.setFont("Helvetica", 10)
    p.drawString(56, height - 105, "Thank you for choosing SkyZone Airlines")
    p.drawRightString(width - 56, height - 105, f"PNR: {booking.pnr}")
    
    # Ticket Content Body
    p.setFillColor(HexColor("#0f172a")) # Dark text
    p.setFont("Helvetica-Bold", 14)
    p.drawString(56, height - 160, "PASSENGER DETAILS")
    
    p.setFont("Helvetica", 10)
    p.setFillColor(HexColor("#475569"))
    p.drawString(56, height - 185, "Passenger Name:")
    p.drawString(220, height - 185, "Nationality:")
    p.drawString(380, height - 185, "Passport Number:")
    
    p.setFillColor(HexColor("#0f172a"))
    p.setFont("Helvetica-Bold", 11)
    p.drawString(56, height - 200, f"{passenger.first_name} {passenger.last_name}")
    p.drawString(220, height - 200, f"{passenger.nationality}")
    p.drawString(380, height - 200, f"{passenger.passport_number}")
    
    # Divider line
    p.setStrokeColor(HexColor("#e2e8f0"))
    p.setLineWidth(1)
    p.line(36, height - 220, width - 72, height - 220)
    
    # Flight details
    p.setFont("Helvetica-Bold", 14)
    p.drawString(56, height - 250, "FLIGHT INFORMATION")
    
    p.setFont("Helvetica", 10)
    p.setFillColor(HexColor("#475569"))
    p.drawString(56, height - 275, "Flight:")
    p.drawString(150, height - 275, "From:")
    p.drawString(280, height - 275, "To:")
    p.drawString(410, height - 275, "Seat:")
    p.drawString(490, height - 275, "Class:")
    
    p.setFillColor(HexColor("#0f172a"))
    p.setFont("Helvetica-Bold", 11)
    p.drawString(56, height - 290, f"{booking.flight.flight_number}")
    p.drawString(150, height - 290, f"{booking.flight.route.origin.city} ({booking.flight.route.origin.code})")
    p.drawString(280, height - 290, f"{booking.flight.route.destination.city} ({booking.flight.route.destination.code})")
    p.drawString(410, height - 290, f"{passenger.seat.seat_number if passenger.seat else 'N/A'}")
    p.drawString(490, height - 290, f"{booking.flight.cabin_class}")
    
    # Dates and Times
    p.setFont("Helvetica", 10)
    p.setFillColor(HexColor("#475569"))
    p.drawString(56, height - 320, "Departure Date/Time:")
    p.drawString(280, height - 320, "Arrival Date/Time:")
    p.drawString(490, height - 320, "Baggage:")
    
    p.setFillColor(HexColor("#0f172a"))
    p.setFont("Helvetica-Bold", 11)
    p.drawString(56, height - 335, f"{booking.flight.departure_time.strftime('%Y-%m-%d %H:%M')}")
    p.drawString(280, height - 335, f"{booking.flight.arrival_time.strftime('%Y-%m-%d %H:%M')}")
    p.drawString(490, height - 335, f"{booking.flight.baggage_allowance}")
    
    # Draw Divider line
    p.line(36, height - 360, width - 72, height - 360)
    
    # Draw QR code on PDF
    # We load the qr code from the memory stream
    qr_buffer.seek(0)
    # Temporary save QR code locally or load as ImageReader to draw
    from reportlab.lib.utils import ImageReader
    qr_reader = ImageReader(qr_buffer)
    p.drawImage(qr_reader, width - 150, height - 500, width=100, height=100)
    
    # Fare Info & Details
    p.setFont("Helvetica-Bold", 14)
    p.drawString(56, height - 390, "TICKET DETAILS & POLICIES")
    p.setFont("Helvetica", 10)
    p.setFillColor(HexColor("#475569"))
    p.drawString(56, height - 415, "Ticket Status:")
    p.drawString(180, height - 415, "Fare Paid:")
    p.drawString(56, height - 440, "Refund Policy:")
    
    p.setFillColor(HexColor("#10b981")) # Success Green
    p.setFont("Helvetica-Bold", 11)
    p.drawString(56, height - 428, "CONFIRMED & PAID")
    p.setFillColor(HexColor("#0f172a"))
    p.drawString(180, height - 428, f"${booking.total_amount}")
    
    p.setFont("Helvetica-Oblique", 9)
    p.drawString(56, height - 455, f"{booking.flight.refund_policy[:100]}...")
    
    # Draw cut line and disclaimer
    p.setStrokeColor(HexColor("#cbd5e1"))
    p.setLineWidth(0.5)
    p.line(36, height - 520, width - 72, height - 520)
    
    p.setFillColor(HexColor("#94a3b8"))
    p.setFont("Helvetica", 8)
    p.drawCentredString(width/2, height - 540, "Please present this e-ticket along with your valid passport at the airport check-in counter.")
    p.drawCentredString(width/2, height - 552, "Gate closes 45 minutes before departure. Have a safe flight!")
    
    p.showPage()
    p.save()
    
    pdf_buffer.seek(0)
    pdf_filename = f"ticket_{ticket_num}.pdf"
    ticket.pdf_file.save(pdf_filename, File(pdf_buffer), save=False)
    
    # Save fields to DB
    ticket.save()
    return ticket
