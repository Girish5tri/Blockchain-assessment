from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlockchainNodeViewSet

router = DefaultRouter()
router.register(r'nodes', BlockchainNodeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]