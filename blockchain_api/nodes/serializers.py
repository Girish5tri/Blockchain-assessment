from rest_framework import serializers
from .models import BlockchainNode

class BlockchainNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockchainNode
        fields = '__all__'