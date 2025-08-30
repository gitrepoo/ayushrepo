from .models import Note, User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class meta:
        model = User
        fields = ('id', 'username', 'email')
        

class NoteSerializer(serializers.ModelSerializer):
    user_details = UserSerializer(read_only = 'true')
    class Meta:
        model = Note
        fields = '__all__'
        read_only_fields = ('id', 'user', 'created_at', 'updated_at')
        
        
                

