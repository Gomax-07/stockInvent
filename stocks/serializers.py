from rest_framework import serializers
from .models import *

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
      fields = (
        'user_id',
        'name',
        'address',
        'created_date',
        'slug',
      )
      model = Supplier


class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
      fields = (
        'user_id',
        'name',
        'address',
        'created_date',
        'slug',
      )
      model = Buyer


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
      fields = (
        'name_id',
        'description',
        'created_date',
        'slug',
      )
      model = Season


class DropSerializer(serializers.ModelSerializer):
    class Meta:
      fields = (
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
        'supplier',
        'product',
        'design',
        'color',
        'buyer',
        'season',
        'drop_id',
        'status',
        'created_date',
        'slug', 
      )
      model = Order

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
      fields = (
        'order_id',
        'courier_name',
        'created_date',
        'slug',
      )
      model = Delivery