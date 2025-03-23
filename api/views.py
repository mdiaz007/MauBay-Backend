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

@api_view(['POST'])
def createListing(request):
    print(request.data['title'])
    # id = models.BigAutoField(primary_key=True)
    # user_id = models.CharField(max_length=100, null=False, blank=False)
    # title = models.TextField(max_length=50, null=False, blank=False)
    # price = models.IntegerField(null=False, blank=False)
    # post_date = models.DateField(auto_now=True)
    # description = models.TextField(max_length=200, null=False, blank=False)
    # quantity = models.IntegerField(null=False, blank=False)

    # # Should be an ImageField!
    # image_url = models.TextField(max_length=200, null=False, blank=False)

    # category = models.CharField(max_length=50, null=False, blank=False, choices=[("Cars", "Cars"),("Jewelry", "Jewelry"),("Clothing", "Clothing")])
    # condition = models.CharField(max_length=50, null=False, blank=False, choices=[("New", "New"),("Used", "Used")])

    # listing_type = models.CharField(max_length=10, default="Active", editable=False, null=False)
    listing = active(user_id=request.data['userID'], title=request.data['title'], image_url=request.data['image'], price=request.data['price'], description=request.data['description'], category=request.data['category'], condition=request.data['condition'])
    listing.save()
    return Response({"Message": "Listing Created!"})


### USER LOGIN OPTIONS

@sync_to_async
def signUp(user_id, firstname, lastname, username, email):
    user = maubay_users(user_id=user_id, firstname=firstname, lastname=lastname, username=username, email=email)
    user.save()