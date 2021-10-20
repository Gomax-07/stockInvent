from rest_framework import serializers
from .models import *

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
      fields = (
        'id',
        'name',
        'address',
        'created_date',
        'slug',
      )
      model = Supplier


class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
      fields = (
        'id',
        'name',
        'address',
        'created_date',
        'slug',
      )
      model = Buyer


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
      fields = (
        'id',
        'description',
        'created_date',
        'slug',
      )
      model = Season


class DropSerializer(serializers.ModelSerializer):
    class Meta:
      fields = (
        'id',
        'name',
        'created_date',
      )
      model = Drop


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
      fields = (
        'name',
        'slug',
        'sortno',
        'created_date',
        
      )
      model = Product

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
      fields = (
        'id',
        'name',
        'supplier',
        'product',
        'design',
        'color',
        'buyer',
        'season',
        'drop',
        'status',
        'created_date',
        'slug', 
      )
      model = Order

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
      fields = (
         'id',
        'order',
        'courier_name',
        'created_date',
        'slug',
      )
      model = Delivery
