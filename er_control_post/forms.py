from django import forms
from .models import post

class PostForm(forms.ModelForm):
	class Meta:
		model = post
		fields = [
			'company',
			'job_title',
			'requirements',
			'content',
			'contact',
		]
		widgets = {
			'company': forms.TextInput(attrs={'style': 'width: 330px'}),
			'job_title': forms.TextInput(attrs={'style': 'width: 330px'}),
			'contact': forms.TextInput(attrs={'style': 'width: 330px'}),
		}