from django.urls import path
from . import views

urlpatterns = [
    path('api/active/', views.getActiveListings),
    path('api/deleted/', views.getDeletedListings),
    path('api/sold/', views.getSoldListings),
    path('api/draft/', views.getDraftListings)
]