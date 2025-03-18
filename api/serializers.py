# from django.contrib.auth.models import Group, User
from .models import active, deleted, draft, sold, maubay_users
from rest_framework import serializers

# Public
# Serializer for the Active model, containing active listings.
class ActiveListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = active
        fields = '__all__'
        # fields = ['id', 'user_id', 'title', 'price', 'post_date', 'description', 'quanitity', 'image_url', 'category', 'condition', 'listing_type']

# Private // May not include
# Serializer for the deleted model, containing deleted listings.
class DeletedListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = deleted
        fields = '__all__'
        # fields = ['id', 'user_id', 'title', 'price', 'post_date', 'description', 'quanitity', 'image_url', 'category', 'condition', 'listing_type']

# Private, attached to user.
# Serializer for the draft model, containing drafted listings.
class DraftListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = draft
        fields = '__all__'
        # fields = ['id', 'user_id', 'title', 'price', 'post_date', 'description', 'quanitity', 'image_url', 'category', 'condition', 'listing_type']

# Public
# Serializer for the sold model, containing sold listings.
class SoldListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = sold
        fields = '__all__'
        # fields = ['id', 'user_id', 'title', 'price', 'post_date', 'description', 'quanitity', 'image_url', 'category', 'condition', 'sell_price', 'sold_date', 'listing_type']

# Private
# Serializer for the user accounts.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = maubay_users
        fields = '__all__'