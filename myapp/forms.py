from django import forms
class Register(forms.Form):
    name=forms.CharField(max_length=30)
    age=forms.IntegerField()