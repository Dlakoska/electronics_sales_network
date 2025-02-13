from rest_framework import serializers
from network.models import NetworkNode, Product


class NetworkNodeSerializer(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        if 'debt' in validated_data:
            raise serializers.ValidationError('Нельзя изменить поле задолженности')
        return super().update(instance, validated_data)

    class Meta:
        model = NetworkNode
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
