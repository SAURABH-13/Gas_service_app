from django.shortcuts import render, redirect
from .forms import ServiceRequestForm, UpdateStatusForm
from django.shortcuts import render
from .models import Customer, ServiceRequest

def index(request):
    # Display list of service requests for the customer
    customer = Customer.objects.get(email=request.user.email)
    service_requests = ServiceRequest.objects.filter(customer=customer)
    return render(request, 'index.html', {'service_requests': service_requests})

def support_dashboard(request):
    # Display list of service requests for customer support reps
    service_requests = ServiceRequest.objects.all()
    return render(request, 'support_dashboard.html', {'service_requests': service_requests})

def submit_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            return redirect('index')  # Redirect to the request tracking page
    else:
        form = ServiceRequestForm()
    return render(request, 'submit_service_request.html', {'form': form})

def track_service_requests(request):
    service_requests = ServiceRequest.objects.filter(customer=request.user)
    return render(request, 'track_service_requests.html', {'service_requests': service_requests})

def update_status(request, request_id):
    service_request = ServiceRequest.objects.get(pk=request_id)

    if request.method == 'POST':
        form = UpdateStatusForm(request.POST, instance=service_request)
        if form.is_valid():
            form.save()
            return redirect('support_dashboard')  # Redirect to support dashboard
    else:
        form = UpdateStatusForm(instance=service_request)
    return render(request, 'update_status.html', {'form': form, 'service_request': service_request})
