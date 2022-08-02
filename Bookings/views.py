from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Bookings
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, InvalidPage


@login_required()
def new_appointment(request):
    if request.method == 'POST':
        email = str(request.user.email)
        form = BookingForm(request.POST)
        if form.is_valid():
            form.cleaned_data['email']= email
            print(form.cleaned_data['email'])
            form.save()
            return redirect('/')
    else:
        form = BookingForm()
    return render(request, 'bookings.html', {'form': form})

@login_required()
def bookings_history(request):
    if request.user.is_staff:
        email = str(request.user.email)
        booking_details = Bookings.objects.all()
        
        print(booking_details)
        return render(request, 'bookings_list.html',{'bookings_details':booking_details})
    else:
        return 1