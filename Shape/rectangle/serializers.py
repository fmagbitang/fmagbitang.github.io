from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *
import datetime, json
from math import *

class RectangleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    width = serializers.CharField(allow_blank=True)
    height = serializers.CharField(allow_blank=True)
    area = serializers.CharField(allow_blank=True, required=False)
    perimeter = serializers.CharField(allow_blank=True, required=False)
    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)
    creator = serializers.ReadOnlyField(source='creator.username')

    def create(self, validated_data):
        """
        Create and return a new `Rectangle` instance, given the validated data.
        """
        width = validated_data['width']
        height = validated_data['height']
        area = int(width) * int(height)
        perimeter = 2 * (int(width) + int(height))
        created_at = datetime.datetime.now()
        updated_at = datetime.datetime.now()

        data = validated_data
        try:
            if data:
                data = validated_data
                data['area'] = area
                data['perimeter'] = perimeter
                data['created_at'] = created_at
                data['updated_at'] = updated_at
        except Exception as e:
            raise
        else:
            pass
        finally:
            pass

        return Rectangle.objects.create(**data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Rectangle` instance, given the validated data.
        """
        instance.width = validated_data.get('width', instance.width)
        instance.height = validated_data.get('height', instance.height)
        instance.area = validated_data.get('height', None)
        instance.perimeter = 2 * (instance.width * instance.height)
        instance.created_at = datetime.datetime.now()
        instance.updated_at = datetime.datetime.now()
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    retangles = serializers.PrimaryKeyRelatedField(many=True, queryset=Rectangle.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'retangles')        