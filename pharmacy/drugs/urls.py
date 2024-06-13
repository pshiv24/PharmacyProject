from django.urls import path
from .views import (
    DrugListCreateView,
    DrugDetailView,
    DrugDeleteView,
    DrugPartialUpdateView,
)

urlpatterns = [
    path("drugs/", DrugListCreateView.as_view(), name="drug-list-create"),
    path("drugs/<int:pk>/", DrugDetailView.as_view(), name="drug-detail"),
    path(
        "drugs/<int:pk>/update/",
        DrugPartialUpdateView.as_view(),
        name="drug-partial-update",
    ),
    path("drugs/<int:pk>/delete/", DrugDeleteView.as_view(), name="drug-delete"),
]
