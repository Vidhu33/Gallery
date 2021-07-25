from taggit.serializers import (TagListSerializerField,TaggitSerializer)
from rest_framework import serializers
from .models import Image


class ImageSerializer(TaggitSerializer, serializers.ModelSerializer):

    tags = TagListSerializerField()

    class Meta:
        model = Image
        fields = '__all__'