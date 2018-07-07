from django import forms
from .models import ChatMessage
from datetime import datetime

class MessageForm(forms.ModelForm):
	class Meta:
		model = ChatMessage
		fields = ('sender', 'receiver','message')
