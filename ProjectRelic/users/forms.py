from django import forms
from .models import Accounts

class Userregestration(forms.ModelForm):
    class Meta:
        model = Accounts
        fields = ['firstname','lastname','e_mail','phone_no']
        widgets = {
            'firstname': forms.TextInput(attrs={'class': ['field ','field1']}), 
        }