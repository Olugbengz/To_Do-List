from django import forms
from .models import To_Do


class NewTask(forms.ModelForm):
	task = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'class':'form-control', 'placeholder':'Task'}), label='')
	start_time = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'class':'form-control', 'placeholder':'Start Time'}), label='')
	end_time = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'class':'form-control', 'placeholder':'End Time'}), label='')
	completed = forms.BooleanField(required=False, widget=forms.widgets.CheckboxInput(attrs={'checked':False}), label='Completed')

	class Meta:
		model = To_Do
		fields = ('task', 'start_time', 'end_time')