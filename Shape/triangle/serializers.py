from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *
import datetime, json
from math import *

class TriangleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    length1 = serializers.CharField(allow_blank=True)
    length2 = serializers.CharField(allow_blank=True)
    length3 = serializers.CharField(allow_blank=True)
    area = serializers.CharField(allow_blank=True, required=False)
    perimeter = serializers.CharField(allow_blank=True, required=False)
    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)
    creator = serializers.ReadOnlyField(source='creator.username')

    def create(self, validated_data):
        """
        Create and return a new `Square` instance, given the validated data.
        """
        length1 = validated_data['length1']
        length2 = validated_data['length2']
        length3 = validated_data['length3']
        sqrt = (int(length1) + int(length2) + int(length3)) / 2
        area = int(sqrt * int(sqrt - int(length1)) * int(sqrt - int(length2)) * int(sqrt - int(length3)) ) ** 0.5
        perimeter = (int(length1) + int(length2) + int(length3))
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

        return Triangle.objects.create(**data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Triangle` instance, given the validated data.
        """
        instance.length1 = validated_data.get('length1', instance.length1)
        instance.length2 = validated_data.get('length1', instance.length2)
        instance.length3 = validated_data.get('length1', instance.length3)
        sqrt = (int(instance.length1) + int(instance.length2) + int(instance.length3))/ 2
        instance.area = int(sqrt * int(sqrt - int(instance.length1)) * int(sqrt - \
            int(instance.length2)) * int(sqrt - int(instance.length3)) ) ** 0.5
        instance.perimeter = int(instance.length1) + int(instance.length2) + int(instance.length3)
        instance.created_at = datetime.datetime.now()
        instance.updated_at = datetime.datetime.now()
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    retangles = serializers.PrimaryKeyRelatedField(many=True, queryset=Triangle.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'retangles')        