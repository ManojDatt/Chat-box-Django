# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import smart_str
from colorfield.fields import ColorField
from django.conf import settings
from session_user.models import ChatUser
class ChatMessage(models.Model):
	class Meta:
		verbose_name = 'Chat Box Message'
		verbose_name_plural = 'Chat Box Messages'

	sender = models.ForeignKey(ChatUser, on_delete=models.CASCADE, related_name="message_sender")
	receiver = models.ForeignKey(ChatUser, on_delete=models.CASCADE, related_name="message_receiver")
	message = models.TextField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now=True)
	seen = models.BooleanField(default=False)


	def __str__(self):
		return smart_str(self.message)
