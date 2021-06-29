from django import forms

class DataForm(forms.ModelForm):
    data= forms.CharField(

        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Search'
            }

        )
    )