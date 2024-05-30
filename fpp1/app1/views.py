from .models import Stage, Answer, Question
from django.http import JsonResponse
from rest_framework import generics
from .models import Stage, Subtage
from .serializers import StageSerializer, SubStageDetailSerializer

class StageListCreateView(generics.ListAPIView):
    queryset = Stage.objects.all()
    serializer_class = StageSerializer

class SubtageDetailView(generics.RetrieveAPIView):
    queryset = Subtage.objects.all()
    serializer_class = SubStageDetailSerializer

