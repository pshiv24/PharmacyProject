# your_app/views.py

from rest_framework import generics
from rest_framework.views import APIView
from .models import Drug
from .serializers import DrugSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from .permissions import DrugPermission


class DrugListCreateView(generics.GenericAPIView):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer
    permission_classes = [DrugPermission]

    def get(self, request, *args, **kwargs):
        queryset = self.queryset
        return Response(queryset.values())

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class DrugDetailView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = DrugSerializer
    permission_classes = [DrugPermission]


class DrugPartialUpdateView(APIView):
    permission_classes = [DrugPermission]

    def patch(self, request, pk, *args, **kwargs):
        try:
            drug = Drug.objects.get(pk=pk)
        except Drug.DoesNotExist:
            return Response(
                {"error": "Drug not found."}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = DrugSerializer(drug, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class DrugDeleteView(APIView):
    permission_classes = [DrugPermission]

    def delete(self, request, pk, *args, **kwargs):
        try:
            drug = Drug.objects.get(pk=pk)
        except Drug.DoesNotExist:
            return Response(
                {"error": "Drug not found."}, status=status.HTTP_404_NOT_FOUND
            )

        drug.delete()
        return Response(
            {"message": "Drug deleted successfully."}, status=status.HTTP_204_NO_CONTENT
        )
