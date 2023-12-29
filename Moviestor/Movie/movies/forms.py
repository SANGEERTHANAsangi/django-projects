from django import forms
from movies.models import nav
class navform(forms.ModelForm):
    class Meta:
        model=nav
        fields='__all__'
