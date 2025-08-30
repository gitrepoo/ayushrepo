from .serializers import NoteSerializer
from rest_framework import viewsets, permissions
from .models import Note, User

# Create your views here.

class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
    def get_queryset(self):
        return Note.objects.filter(user = self.request.user).order_by('-updated_at')
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    

