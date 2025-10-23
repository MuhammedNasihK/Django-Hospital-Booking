from django import forms
from .models import Booking

class Datefield(forms.DateInput):
    input_type = 'date'

class Bookingform(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'booking_date' : Datefield(),
        }

        labels = {
            'p_name' : 'Patient Name:',
            'p_phone' : 'Phone No:',
            'p_email' : 'Email ID:',
            'doc_name' : 'Select Doctor:',
            'booking_date' : 'Booking Date:'
        }
