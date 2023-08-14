from django.urls import path
from . import views

urlpatterns = [
    path('', views.track_service_requests, name='index'),
    path('submit/', views.submit_service_request, name='submit_service_request'),
    path('track/', views.track_service_requests, name='track_service_requests'),
    path('update_status/<int:request_id>/', views.update_status, name='update_status'),
    path('support/', views.support_dashboard, name='support_dashboard'),
    # Add more URLs as needed
]
