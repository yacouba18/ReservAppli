from django import forms
from .models import Evenement

class EvenementForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control datepicker'}))
    start_time = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control timepicker'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control datepicker'}))
    end_time = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control timepicker'}))

    class Meta:
        model = Evenement
        fields = ['name', 'start_date', 'start_time', 'end_date', 'end_time']