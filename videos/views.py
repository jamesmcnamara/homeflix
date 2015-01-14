from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from videos.models import Video
from videos.serializers import VideosSerializer


class HomePage(generics.RetrieveAPIView):
    queryset = Video.objects.all()
    renderer_classes = (TemplateHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        return Response(template_name="base.html")


class VideoViewSet(ModelViewSet):
    queryset = Video.objects.all()
    renderer_classes = (JSONRenderer,)
    serializer_class = VideosSerializer