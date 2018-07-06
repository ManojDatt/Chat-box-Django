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
			mobile = request.POST['mobile']
			password = request.POST['password']
			user = authenticate(mobile=mobile, password=password)

			if user is not None:
				if user.is_active:
					login(request, user)
					return  HttpResponse("Login Success")
				else:
					return HttpResponse("Inactive user.")
			else:
				return  HttpResponse("Invalid Login User.")
		else:
			return  HttpResponse("Invalid Login Details.")

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('new_session')


class SignupView(View):
	def post(self, request, *args, **kwargs):
		form = RegistrationForm(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.is_active = True
			obj.save()
			obj.set_password(form.cleaned_data['password'])
			login(request, obj)
			return  HttpResponse("Sign Up Success")
		else:
			return  HttpResponse("Invalid Signup Details.")
