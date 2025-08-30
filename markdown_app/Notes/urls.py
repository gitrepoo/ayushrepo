from .views import NoteViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'not', NoteViewSet, basename='Note')

urlpatterns = [
    path('', include(router.urls)),
]
