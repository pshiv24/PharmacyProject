from rest_framework import generics, permissions
from .models import Order
from users.models import User
from drugs.models import Drug
from .serializers import OrderSerializer,OrderPostSerializer
from rest_framework.response import Response
from rest_framework import status


class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = request.data
        drug = Drug.objects.get(id=data.get("drug_id"))
        user = User.objects.get(username=data.get("username"))

        serializer_data = {
            "username": user.id,
            "drug_id": drug.id,
            "quantity": data.get("quantity"),
        }

        serializer = OrderPostSerializer(data=serializer_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response_data = serializer.data
        response_data["username"] = user.username

        return Response(response_data, status=status.HTTP_201_CREATED)


class OrderRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Order.objects.all()
        return Order.objects.filter(username=self.request.user)


class OrderStatusUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        try:
            order = self.get_object()
        except Order.DoesNotExist:
            return Response(
                {"error": "Order not found."}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(order, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
