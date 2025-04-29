from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from .serializers import SegmentationSerializer
from .api import predire_segment
from django.shortcuts import render
from .api import predire_segment


class SegmentationViewSet(viewsets.ViewSet):
    
    @action(detail=False, methods=['post'])
    def post(self, request):
        serializer = SegmentationSerializer(data=request.data)
        if serializer.is_valid():
            age = serializer.validated_data['age']
            revenu = serializer.validated_data['revenu']
            score = serializer.validated_data['score']
            segment = predire_segment(age, revenu, score)
            return Response({"segment": segment}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
def formulaire_prediction(request):
    segment = None

    if request.method == 'POST':
        age = request.POST.get('age')
        revenu = request.POST.get('revenu')
        score = request.POST.get('score')

        try:
            age = float(age)
            revenu = float(revenu)
            score = float(score)
            segment = predire_segment(age, revenu, score)
        except:
            segment = "Erreur : vérifiez les valeurs saisies."

    return render(request, 'segmentation/formulaire.html', {'segment':segment})