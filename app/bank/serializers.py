from .models import Branch, Customer
from rest_framework import serializers

class Branch_Serializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Branch
        fields = [
            'location_name',
            'location'
        ]

class Customer_Serializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Customer
        fields = [
            'customer_name',
            'customer_email',
            'branch_id'
        ]