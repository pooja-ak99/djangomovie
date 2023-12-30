from django import forms
from Movies.models import movie

class movieform(forms.ModelForm):
    class Meta:
        model = movie
        fields = '__all__'