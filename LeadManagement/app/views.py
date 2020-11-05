from django.shortcuts import render
from .forms import LeadForms
from .models import Lead

# Create your views here.
def showHome(request):
    qs = Lead.objects.all()
    return render(request,'home.html',{'qs':qs})

def showDisplay(request):
    source = request.GET['source']
    phone_number = request.GET['phone_number']
    response = request.GET['response']
    date_of_followup = request.GET['date_of_followup']
    return render(request, 'display.html', {'source':source,'phone_number':phone_number,'response':response,'date_of_followup':date_of_followup})