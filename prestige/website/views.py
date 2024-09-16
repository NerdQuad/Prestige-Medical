from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "base.html")

def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")

def specialties(request):
    return render(request, "specialties.html")

def teams(request):
    return render(request, "teams.html")

def appointment(request):
    return render(request, "appointment.html")

def contact(request):
    return render(request, "contact.html")
