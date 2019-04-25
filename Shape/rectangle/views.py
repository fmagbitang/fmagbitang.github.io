from .models import Rectangle
from .serializers import RectangleSerializer
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

class RectangleList(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    """
    List all snippets, or create a new rectangle.
    """
    def get(self, request, format=None):
        rectangles = Rectangle.objects.all()
        serializer = RectangleSerializer(rectangles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RectangleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RectangleDetail(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    """
    Retrieve, update or delete a rectangle instance.
    """
    def get_object(self, pk):
        try:
            return Rectangle.objects.get(pk=pk)
        except Rectangle.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        rectangle = self.get_object(pk)
        serializer = RectangleSerializer(rectangle)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        rectangle = self.get_object(pk)
        serializer = RectangleSerializer(rectangle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        rectangle = self.get_object(pk)
        rectangle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)