from rest_framework import serializers
from .models import ChatMessage


class ChatMessageSerializer(serializers.ModelSerializer):
    sendon = serializers.SerializerMethodField()
    class Meta:
        model = ChatMessage
        fields = '__all__'

    def get_sendon(self, obj):
        return obj.created_at.strftime('%H:%M %p, %d %B %Y')