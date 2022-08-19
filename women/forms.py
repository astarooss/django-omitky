from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={'placeholder': 'jmeno a primeni', 'class': 'form_p'}))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'E-mail', 'class': 'form_p'}))
    phone = forms.CharField(
        max_length=15,
        widget=forms.NumberInput(
            attrs={'placeholder': 'Telefonní číslo', 'class': 'form_p'}))
    message = forms.CharField(
        min_length=10,
        widget=forms.Textarea(
            attrs={'placeholder': 'Sprava', 'cols': 30, 'rows': 9, 'class': 'form-control w-100', 'name': '.'}))
    
