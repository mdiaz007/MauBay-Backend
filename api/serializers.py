# from django.contrib.auth.models import Group, User
from .models import active, deleted, draft, sold
from rest_framework import serializers

# Public
# Serializer for the Active model, containing active listings.
class ActiveListingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = active
        Fields = []

# Private // May not include
# Serializer for the deleted model, containing deleted listings.
class DeletedListingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = deleted
        Fields = []

# Private, attached to user.
# Serializer for the draft model, containing drafted listings.
class DraftListingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = draft
        Fields = []

# Public
# Serializer for the sold model, containing sold listings.
class SoldListingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = sold
        Fields = []
