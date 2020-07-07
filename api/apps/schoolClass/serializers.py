from rest_framework import serializers
from .models import Class

class ClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = Class
        fields = ('pk', 'name', 'name_subclass')


class ClassPersistSerializer(serializers.Serializer):

    name = serializers.CharField(required=True)
    name_subclass = serializers.CharField(required=False)

    def create(self):
        return Class.objects.create(**self.validated_data)