from django.core import validators
from django import forms
from .models import User_table


class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User_table
        fields = ['brand', 'invamt', 'invdate','cltnamt', 'cltndate', 'customer', 'customercode', 'collectedby', 'paymentmode', 'cheque', 'bank', 'duedate', 'status', 'doptdate', 'utrno', 'bksc']
        widgets = {
            'brand' : forms.TextInput(attrs={'class':'form-control'}),
            'invamt' : forms.TextInput(attrs={'class':'form-control'}),
            'invdate': forms.DateInput(attrs={'class': 'form-control'}),
            'cltnamt' : forms.TextInput(attrs={'class':'form-control'}),
            'cltndate' : forms.DateInput(attrs={'class': 'form-control'}),
            'customer' : forms.TextInput(attrs={'class':'form-control'}),
            'customercode' : forms.TextInput(attrs={'class':'form-control'}),
            'collectedby' : forms.TextInput(attrs={'class':'form-control'}),
            'paymentmode' : forms.TextInput(attrs={'class':'form-control'}),
            'cheque' : forms.TextInput(attrs={'class':'form-control'}),
            'bank' : forms.TextInput(attrs={'class':'form-control'}),
            'duedate': forms.DateInput(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
            'doptdate': forms.DateInput(attrs={'class': 'form-control'}),
            'utrno': forms.TextInput(attrs={'class': 'form-control'}),
            'bksc': forms.TextInput(attrs={'class': 'form-control'}),   
        }


 
