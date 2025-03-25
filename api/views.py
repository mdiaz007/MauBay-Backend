from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import active, deleted, sold, draft, maubay_users
from .serializers import ActiveListingSerializer
from .serializers import DeletedListingSerializer
from .serializers import SoldListingSerializer
from .serializers import DraftListingSerializer
from asgiref.sync import sync_to_async
import os

# General
@api_view(['GET'])
def getActiveListings(request):
    actives = active.objects.all()
    serializer = ActiveListingSerializer(actives, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSoldListings(request):
    solds = sold.objects.all()
    serializer = SoldListingSerializer(solds, many=True)
    print(serializer)
    return Response(serializer.data)

# Dashboard
@api_view(['GET'])
def getUserActive(request):
    user_id = request.GET.get('id')
    actives = active.objects.filter(user_id=user_id)
    serializer = ActiveListingSerializer(actives, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getUserSold(request):
    user_id = request.GET.get('id')
    solds = sold.objects.filter(user_id=user_id)
    serializer = SoldListingSerializer(solds, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getUserDraft(request):
    user_id = request.GET.get('id')
    drafted = draft.objects.filter(user_id=user_id)
    serializer = DraftListingSerializer(drafted, many=True)
    return Response(serializer.data)

# Listing 
@api_view(['POST'])
def createListing(request):
    listing = active(user_id=request.data['userID'], title=request.data['title'], image_url=request.data['image'], price=request.data['price'], description=request.data['description'], category=request.data['category'], condition=request.data['condition'])
    listing.save()
    return Response({"Message": "Listing Created!"})

@api_view(['POST'])
def createDraft(request):
    listing = draft(user_id=request.data['userID'], title=request.data['title'], image_url=request.data['image'], price=request.data['price'], description=request.data['description'], category=request.data['category'], condition=request.data['condition'])
    listing.save()
    return Response({"Message": "Draft Created!"})


# User Login Options
@sync_to_async
def signUp(user_id, firstname, lastname, username, email):
    user = maubay_users(user_id=user_id, firstname=firstname, lastname=lastname, username=username, email=email)
    user.save()