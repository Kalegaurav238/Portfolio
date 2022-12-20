from django import forms

class usersdata (forms.Form):
    num1 = forms.CharField(label='value 1',widget=forms.TextInput(attrs={'class':"form-control"}))
    num2 = forms.CharField(label='value 2',widget=forms.PasswordInput(attrs={'class':"form-control"}))
