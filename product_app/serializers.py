from rest_framework import serializers
from .models import *


class TokenModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['user_id']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'cost_per_item', 'stock_quantity', 'volume']
        read_only_fields = ['volume']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        return user