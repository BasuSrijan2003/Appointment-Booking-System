from django.shortcuts import render
from django.core.mail import send_mail
from Appointment.models import Appointments
from django.db import connection

# Create your views here.
def index(request):
    if request.method == "POST":
        message = request.POST['message']
        guests = request.POST['guests']
        children = request.POST['children']
        date = request.POST['date']
        time = request.POST['time']
        email = request.POST['email']

        """send_mail(
            'Book Appointment', #subject
            message, #message
            email, #from email
            ['gsouvik407@gmail.com'], #to email
        )"""

        ins = Appointments(Name = message, Guests = guests, Children = children, Date = date, Time = time, Email = email)
        ins.save()
        
        return render(request, "index.html", {'message' : message, 'guests' : guests, 
                                              'children' : children, 'date' : date, 'time' : time, 'email' : email})
    else:
        return render(request, "index.html", {})