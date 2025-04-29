from django.urls import path, include
from rest_framework.routers import DefaultRouter # type: ignore
from .views import SegmentationViewSet, formulaire_prediction

router = DefaultRouter()
router.register('segmentation', SegmentationViewSet, basename='segmentation')

urlpatterns = [
    path('api/', include(router.urls)), 
    path('', formulaire_prediction, name='formulaire-prediction'),
    path('predict/', SegmentationViewSet.as_view({'post': 'create'}), name='predict-segment'),

]