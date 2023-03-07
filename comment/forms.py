from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'bid', 'reply_to_id']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
            'bid': forms.HiddenInput(),
            'reply_to_id': forms.HiddenInput(),
        }