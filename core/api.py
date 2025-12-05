from rest_framework import viewsets, permissions
from .models import Product, Client, Order
from .serializers import ProductSerializer, ClientSerializer, OrderSerializer
from .permissions import IsOwner, IsCashier, IsSalesAssociate

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsSalesAssociate]

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsCashier]
