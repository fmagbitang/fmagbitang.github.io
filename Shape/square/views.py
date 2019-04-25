from .models import Square
from .serializers import SquareSerializer
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

class SquareList(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    """
    List all snippets, or create a new square.
    """
    def get(self, request, format=None):
        squares = Square.objects.all()
        serializer = SquareSerializer(squares, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SquareSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SquareDetail(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    """
    Retrieve, update or delete a square instance.
    """
    def get_object(self, pk):
        try:
            return Square.objects.get(pk=pk)
        except Square.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        square = self.get_object(pk)
        serializer = SquareSerializer(square)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        square = self.get_object(pk)
        serializer = SquareSerializer(square, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        square = self.get_object(pk)
        square.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)