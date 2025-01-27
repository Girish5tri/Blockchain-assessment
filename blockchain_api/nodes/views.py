from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import BlockchainNode
from .serializers import BlockchainNodeSerializer
from rest_framework import permissions


class BlockchainNodeViewSet(viewsets.ModelViewSet):
    queryset = BlockchainNode.objects.all()
    serializer_class = BlockchainNodeSerializer
    permission_classes = [permissions.AllowAny]
