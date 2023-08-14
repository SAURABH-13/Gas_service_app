from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['request_type', 'details', 'attached_files']

class UpdateStatusForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['status']

