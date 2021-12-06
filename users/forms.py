from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.modelfields import PhoneNumberField
from .models import Profile

class RegistrationForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields=['username','email','password1','password2']



class UserUpdateForm(forms.ModelForm):
	email = models.EmailField()

	class Meta:
		model = User
		fields=['username','email']



class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields=['image']

