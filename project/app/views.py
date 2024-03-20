from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ServiceRequest
from .forms import ServiceRequestForm


def submit_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            if request.user.is_authenticated:
                service_request = form.save(commit=False)
                service_request.customer_id = request.user.id
                service_request.save()
                return HttpResponse("Service request submitted successfully.")
            else:
                return HttpResponse("You need to be logged in to submit a service request.", status=401)
    else:
        form = ServiceRequestForm()
    return render(request, 'submit_service_request.html', {'form': form})


def track_service_request(request, request_id):
    try:
        service_request = ServiceRequest.objects.get(pk=request_id)
    except ServiceRequest.DoesNotExist:
        return HttpResponse("Invalid request ID.")

    return render(request, 'track_service_request.html', {'service_request': service_request})



