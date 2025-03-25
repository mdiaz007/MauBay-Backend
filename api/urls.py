from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/active/', views.getActiveListings),
    path('api/sold/', views.getSoldListings),
    path('api/user/active/', views.getUserActive),
    path('api/user/sold/', views.getUserSold),
    path('api/user/draft/', views.getUserDraft),
    path('api/listing/add', views.createListing),
    path('api/listing/draft', views.createDraft),
    # path('api/listing/delete', views.deleteListing),
    # path('api/listing/sold', views.soldListing)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)