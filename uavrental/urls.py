"""
URL configuration for uavrental project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from rentals.views import UAVListCreateView, UAVDetailView, RentalListCreateView, RentalDetailView, UserListCreateView, UserDetailView

urlpatterns = [
    path('api/users/', UserListCreateView.as_view(), name='user-list-create'),
    path('api/users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('api/uavs/', UAVListCreateView.as_view(), name='uav-list-create'),
    path('api/uavs/<int:pk>/', UAVDetailView.as_view(), name='uav-detail-update'),
    path('api/rentals/', RentalListCreateView.as_view(), name='rental-list'),
    path('api/rentals/', RentalListCreateView.as_view(), name='rental-create'),
    path('api/rentals/<int:pk>/', RentalDetailView.as_view(), name='rental-detail-update-delete'),
]

