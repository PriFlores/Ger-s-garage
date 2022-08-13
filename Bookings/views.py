from datetime import datetime
from shop_cart.views import add_cart
from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Bookings
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, InvalidPage

def bkPay(request): ## render the payment for bookings
    return render(request,'PayForBooking.html')
@login_required() ## to unsure the user is authenticated
def new_appointment(request): ## to make an appointment
    if request.method == 'POST': ## to post the data that is in the form
        form = BookingForm(request.POST) ## booking form with the data filled in it
        if form.is_valid(): ## validating the form
            form.save() ## saving th form and creating the booking object
            return redirect('Pay_BK') ## it will redirect the user to a payment page
    else:
        form = BookingForm() ## if it is not a post it will create a new form to be filled
    return render(request, 'bookings.html', {'form': form})

@login_required()
def bookings_history(request): ## function for th booking history
    if request.user.is_staff or request.user.is_superuser: # only available for the administrator (super user) or staff, clients will not be able to see this part
        email = str(request.user.email) ## converting the request bits for email into string format
        booking_details = Bookings.objects.all() ## to see all the bookings
        for booking in booking_details: ## looping for every booking
            if booking.date == datetime.now():## if the booking is today the status will be 1
                booking.status = 1 ## 1 means in progresss
                booking.save() ## saving its interaction of the booking
        return render(request, 'bookings_list.html',{'bookings_details':booking_details}) ## return the book list
    else:
        return 1 ## placeholder