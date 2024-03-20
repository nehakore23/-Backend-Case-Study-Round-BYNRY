from django.urls import path
from . import views

urlpatterns = [
    path('', views.submit_service_request, name='submit_service_request'),
    path('<int:request_id>/', views.track_service_request, name='track_service_request'),

]
