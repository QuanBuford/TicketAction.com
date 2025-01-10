from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['author','title', 'description', 'date', 'location', 'price']

class TicketPurchaseForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, label="Number of Tickets")