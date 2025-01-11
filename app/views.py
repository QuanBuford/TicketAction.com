from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Event, Ticket
from .forms import EventForm, TicketPurchaseForm

# Create your views here.
def home(request):
    return render(request, "home.html")

def login_PAGE(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('event_list') 
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def register_PAGE(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'register.html')
        
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        messages.success(request, "Account created successfully!")
        return redirect('Login')

    return render(request, 'register.html')

def logout_PAGE(request):
    logout(request)
    return redirect('home')

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

def view_events(request):
    events = Event.objects.all() 
    return render(request, 'events.html', {'events': events})

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event added successfully.')
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'add_event.html', {'form': form})

def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated successfully.')
            return redirect('event_list')
    else:
        form = EventForm(instance=event)
    return render(request, 'edit_event.html', {'form': form, 'event': event})

def remove_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.delete()
    messages.success(request, 'Event removed successfully.')
    return redirect('event_list')

def purchase_ticket(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = TicketPurchaseForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            total_price = quantity * event.price
            ticket, created = Ticket.objects.get_or_create(
                user=request.user,
                event=event,
                defaults={'quantity': 0}
            )
            ticket.quantity += quantity
            ticket.save()
            messages.success(request, f'Successfully purchased {quantity} tickets for {event.title}. Total: ${total_price:.2f}')
            return redirect('event_list')
    else:
        form = TicketPurchaseForm()
    return render(request, 'purchase_ticket.html', {'event': event, 'form': form})


def user_tickets(request):
    tickets = Ticket.objects.filter(user=request.user)
    return render(request, 'user_tickets.html', {'tickets': tickets})
