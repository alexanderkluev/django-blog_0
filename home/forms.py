from django import forms
from .models import Comment

class CommenForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
class EmailForm(forms.Form):
    email = forms.EmailField()