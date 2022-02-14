from django.shortcuts import render
from passengerApp.models import Passenger


# Create your views here.
def passengerData(request):
    passengers = Passenger.objects.all()
    passengers_dictionary = {"passengers": passengers}
    return render(request, "passengerApp/passengers-list.html", passengers_dictionary)
