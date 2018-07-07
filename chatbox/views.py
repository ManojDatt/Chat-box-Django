# -*- coding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse
from session_user.models import ChatUser
from .forms import MessageForm
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.utils.decorators import method_decorator
import json
from .serializers import ChatMessageSerializer
from .models import ChatMessage

class ChatBoxList(LoginRequiredMixin, ListView):
    template_name = 'chat-list.html'
    model = ChatUser

    def get_context_data(self, **kwargs):
        context = super(ChatBoxList, self).get_context_data(**kwargs)
        context['list_user'] = ChatUser.objects.filter(is_staff=False).exclude(id=self.request.user.id)
        return context


class CreateMessageView(LoginRequiredMixin, View):
	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super(CreateMessageView, self).dispatch(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		form = MessageForm(request.POST)
		if form.is_valid():
			obj = form.save()
			response_data = {"message": "Message send", "code": 200, "message_id": obj.id }
			return HttpResponse(json.dumps(response_data), content_type="application/json")
		else:
			response_data = {"message": "Invalid Message Data", "code": 500}
			return HttpResponse(json.dumps(response_data), content_type="application/json")


class LoadMessagesViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
	""" this functionis used to get all messages between sender and receiver 
	when user select any user from list for conversations """
	queryset = ChatMessage.objects.all()
	serializer_class = ChatMessageSerializer

	def get_queryset(self):
		sender = self.request.user.id
		receiver = self.kwargs['receiver']
		queryset = ChatMessage.objects.filter(sender_id__in=[sender, receiver], receiver_id__in=[receiver,sender]).order_by('-id')[:50]
		return queryset