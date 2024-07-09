from django.shortcuts import render
from django.http import HttpResponse

def book_room(request):
    if request.method == "POST":


        name = request.POST.get('name')
        date = request.POST.get('date')

        return render(request, 'booking_confirmation.html', {'name': name, 'date': date})
    return render(request, 'booking_form.html')

def booking_confirmation(request):

    return render(request, 'booking_confirmation.html')