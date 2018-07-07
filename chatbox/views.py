# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpResponse
from session_user.models import ChatUser
from .forms import MessageForm

class ChatBoxList(LoginRequiredMixin, ListView):
    template_name = 'chat-list.html'
    model = ChatUser

    def get_context_data(self, **kwargs):
        context = super(ChatBoxList, self).get_context_data(**kwargs)
        context['list_user'] = ChatUser.objects.filter(is_staff=False).exclude(id=self.request.user.id)
        return context


class CreateMessageView(View):
	def post(self, request, *args, **kwargs):
		form = MessageForm(request.POST)
		if form.is_valid():
			form.save()
			response_data = {"message": "Sign Up Success", "code": 200}
			return HttpResponse(json.dumps(response_data), content_type="application/json")
		else:
			response_data = {"message": "Invalid Data", "code": 500}
			return HttpResponse(json.dumps(response_data), content_type="application/json")
