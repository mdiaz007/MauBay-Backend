from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/active/', views.getActiveListings),
    path('api/deleted/', views.getDeletedListings),
    path('api/sold/', views.getSoldListings),
    path('api/draft/', views.getDraftListings),
    path('api/listing/add', views.createListing),
    # path('api/listing/draft', views.createListing),
    # path('api/listing/delete', views.createListing),
    # path('api/listing/sold', views.createListing)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)