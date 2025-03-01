from django.urls import path
from . import views

urlpatterns = [
    path('active/', views.getActiveListings),
    path('deleted/', views.getDeletedListings),
    path('sold/', views.getSoldListings),
    path('draft/', views.getDraftListings)
]