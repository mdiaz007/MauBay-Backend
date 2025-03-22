from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import active, deleted, sold, draft, maubay_users
from .serializers import ActiveListingSerializer
from .serializers import DeletedListingSerializer
from .serializers import SoldListingSerializer
from .serializers import DraftListingSerializer
from asgiref.sync import sync_to_async

# GET Requests
@api_view(['GET'])
def getActiveListings(request):
    actives = active.objects.all()
    serializer = ActiveListingSerializer(actives, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getDeletedListings(request):
    delete = deleted.objects.all()
    serializer = DeletedListingSerializer(delete, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSoldListings(request):
    solds = sold.objects.all()
    serializer = SoldListingSerializer(solds, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getDraftListings(request):
    drafted = draft.objects.all()
    serializer = DraftListingSerializer(drafted, many=True)
    return Response(serializer.data)

@sync_to_async
def signUp(user_id, firstname, lastname, username, email):
    test = maubay_users(user_id=user_id, firstname=firstname, lastname=lastname, username=username, email=email)
    test.save()