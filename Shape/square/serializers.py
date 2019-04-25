from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *
import datetime, json
from math import *

class SquareSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    side = serializers.CharField(allow_blank=True)
    area = serializers.CharField(allow_blank=True, required=False)
    perimeter = serializers.CharField(allow_blank=True, required=False)
    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)
    creator = serializers.ReadOnlyField(source='creator.username')

    def create(self, validated_data):
        """
        Create and return a new `Square` instance, given the validated data.
        """
        side = validated_data['side']
        area = int(side) * int(side)
        perimeter = 4 * (int(side))
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

        return Square.objects.create(**data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Square` instance, given the validated data.
        """
        instance.side = validated_data.get('side', instance.side)
        instance.area = int(instance.side) * int(instance.side)
        instance.perimeter = 4 * (instance.side)
        instance.created_at = datetime.datetime.now()
        instance.updated_at = datetime.datetime.now()
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    retangles = serializers.PrimaryKeyRelatedField(many=True, queryset=Square.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'retangles')        