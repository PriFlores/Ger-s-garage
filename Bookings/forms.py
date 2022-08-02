from datetime import date, datetime
from django import forms
from datetimewidget.widgets import DateTimeWidget
from django.forms import ModelForm, TextInput, DateInput, Select

from .models import Bookings


class BookingForm(ModelForm):
    class Meta:
        model = Bookings
        fields = ('staff', 'date', 'timeslot', 'CustName', 'Reg', 'type', 'number', 'email', 'VehicleType', 'CarMake',
                  'EngineType')
        widgets = {
            'staff': Select(attrs={'class': "form-control",'placeholder': 'Staff'}),
            'date': DateInput(
                attrs={ 'type': 'date', 'value': datetime.now().strftime("%d-%m-%Y"),
                       'class': 'form-control','style': 'max-width: 300px;'},
            ),

            'timeslot': Select(attrs={
                'class': "form-control",
                'placeholder': 'Name',
                'style': 'max-width: 190px;',
            }),
            'CustName': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Name',
                'style': 'max-width: 300px;',
            }),
            'Reg': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Name',
                'style': 'max-width: 190px;',
            }),
            'type': Select(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
            }),
            'number': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
            }),
            'VehicleType': Select(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
            }),
            'CarMake': Select(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
            }),
            'EngineType': Select(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
            }),
        }

    def clean_date(self):
        day = self.cleaned_data['date']

        if day <= date.today():
            raise forms.ValidationError('Date should be upcoming(tomorrow or later)', code='invalid')
        if day.isoweekday():
            return day
        else:
            raise forms.ValidationError('Unfortunately we are not open on Sundays', code='invalid')
