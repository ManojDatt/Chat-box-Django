# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.encoding import smart_str
from colorfield.fields import ColorField

class UserManager(BaseUserManager):
	""" In order to have mobile number as username you have to remove username field"""
	use_in_migrations = True
	def _create_user(self, email, password, **extra_fields):
		if not email:
			raise ValueError('The given email must be set')
			email = self.normalize_email(email)
			user = self.model(email=email, **extra_fields)
			user.set_password(password)
			user.save(using=self._db)
			return user
	def create_superuser(self, email, password, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError('Superuser must have is_staff=True.')
		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser=True.')

		return self._create_user(email, password, **extra_fields)

class ChatUser(AbstractUser):
	class Meta:
		verbose_name = 'Chat Box User'
		verbose_name_plural = 'Chat Box Users'
	mobile = models.CharField(verbose_name='Mobile Number', max_length=20, null=False, blank=False, unique=True)
	color_code = ColorField(verbose_name='User Color Code', blank=True, null=True)
	date_of_birth = models.DateField(verbose_name='Date Of Birth', null=True)

	def __str__(self):
		return smart_str(self.username)

	def save(self, *args, **kwargs):
		if self.password:
			self.set_password(self.password)
		super(ChatUser, self).save(*args, **kwargs)


