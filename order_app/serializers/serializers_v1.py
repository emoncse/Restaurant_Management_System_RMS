from rest_framework import serializers
from order_app.models import Orders


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        exclude = ["created_at", "updated_at", "is_active"]
