from django import forms

class WeatherForm(forms.Form):
    city = forms.CharField(max_length=500, required=True,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter City: '}))
    