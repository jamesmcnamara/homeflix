__author__ = 'james'

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from videos.models import Video


class VideosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video