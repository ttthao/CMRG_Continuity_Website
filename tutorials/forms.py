from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        widgets = {'tutorial': forms.HiddenInput()}
        fields = [
            'rating',
            'subject',
            'comment',
            'tutorial'
        ]
