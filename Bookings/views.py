from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Bookings
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, InvalidPage


@login_required()
def new_appointment(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BookingForm()
    return render(request, 'bookings.html', {'form': form})
