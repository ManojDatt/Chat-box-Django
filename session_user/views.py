# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegistrationForm
from django.http import HttpResponse
import json

class SessionView(TemplateView):
    def get(self, request, *args, **kwargs):
        context = {"login_form": LoginForm,
                   "registration_form": RegistrationForm
                    }
        return render(request, 'login_registration.html', context)

class LoginView(View):
	def post(self, request, *args, **kwargs):
		form = LoginForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(request, username=username, password=password)

			if user is not None:
				if user.is_active:
					login(request, user)
					response_data = {"message": "Login Up Success", "code": 200}
					return HttpResponse(json.dumps(response_data), content_type="application/json")
				else:
					response_data = {"message": "Inactive user.", "code": 500}
					return HttpResponse(json.dumps(response_data), content_type="application/json")
			else:
				response_data = {"message": "Invalid Login User.", "code": 500}
				return  HttpResponse(json.dumps(response_data), content_type="application/json")
		else:
			response_data = {"message": "Invalid Login Details.", "code": 500}
			return HttpResponse(json.dumps(response_data), content_type="application/json")

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')


class SignupView(View):
	def post(self, request, *args, **kwargs):
		import datetime
		data = request.POST.copy()
		data['date_joined'] = datetime.date.today()
		form = RegistrationForm(data)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.is_active = True
			obj.save()
			login(request, obj)
			response_data = {"message": "Sign Up Success", "code": 200}
			return HttpResponse(json.dumps(response_data), content_type="application/json")
		else:
			response_data = {"message": "Invalid Data", "code": 500}
			return HttpResponse(json.dumps(response_data), content_type="application/json")
