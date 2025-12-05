from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import ProductViewSet, ClientViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
