# your_app/urls.py

from django.urls import path
from .views import OrderListCreateView, OrderRetrieveUpdateView, OrderStatusUpdateView

urlpatterns = [
    path("orders/", OrderListCreateView.as_view(), name="order-list-create"),
    path("orders/<int:pk>/", OrderRetrieveUpdateView.as_view(), name="order-detail"),
    path(
        "orders/<int:pk>/update/",
        OrderStatusUpdateView.as_view(),
        name="order-status-update",
    ),
]
