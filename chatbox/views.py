# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.views import View
from .forms import LoginForm, RegistrationForm

class SessionView(TemplateView):
    def get(self, request, *args, **kwargs):
        context = {"login_form": LoginForm,
                   "registration_form": RegistrationForm
                    }
        return render(request, 'login_registration.html', context)