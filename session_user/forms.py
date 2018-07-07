from django import forms
from .models import ChatUser
from datetime import datetime

class LoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(), required=True, max_length=100)



class RegistrationForm(forms.ModelForm):
	confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Enter Confirm Password'}))
	class Meta:
		model = ChatUser
		fields = '__all__'
		widgets = {
		'username': forms.TextInput(attrs={'class': 'form-control','placeholder': 'User Name'}),
		'date_joined': forms.HiddenInput(attrs={'value': datetime.now(), 'readonly': True}),
		'date_of_birth': forms.TextInput(attrs={'class': 'form-control date_field','placeholder': 'Enter date Of Birth'}),
		'mobile': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Mobile Number'}),
		'password': forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Enter Password'}),
		}

	def clean(self):
		cleaned_data = super(RegistrationForm, self).clean()
		password = cleaned_data.get("password")
		confirm_password = cleaned_data.get("confirm_password")
		if password != confirm_password:
			raise forms.ValidationError("Password and Confirm password does not match")