from .models import Triangle
from .serializers import TriangleSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from django.contrib.auth.models import User
from .serializers import UserSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TriangleList(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    """
    List all snippets, or create a new triangle.
    """
    def get(self, request, format=None):
        triangles = Triangle.objects.all()
        serializer = TriangleSerializer(triangles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TriangleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TriangleDetail(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    """
    Retrieve, update or delete a triangle instance.
    """
    def get_object(self, pk):
        try:
            return Triangle.objects.get(pk=pk)
        except Triangle.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        triangle = self.get_object(pk)
        serializer = TriangleSerializer(triangle)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        triangle = self.get_object(pk)
        serializer = TriangleSerializer(triangle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        triangle = self.get_object(pk)
        triangle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)