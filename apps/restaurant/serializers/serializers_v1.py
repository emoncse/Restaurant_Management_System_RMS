from rest_framework import serializers
from ..models import Restaurant, Employee, Menu, MenuItem
from apps.user.serializers.serializers_v1 import UserListSerializer

class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        exclude = ["created_at", "updated_at"]


class EmployeeListSerializer(serializers.ModelSerializer):
    user = UserListSerializer(read_only=True, required=False)

    class Meta:
        model = Employee
        exclude = ["created_at", "updated_at"]

class EmployeeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Employee
        exclude = ["created_at", "updated_at"]


class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        exclude = ["created_at", "updated_at"]


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        exclude = ["created_at", "updated_at"]
