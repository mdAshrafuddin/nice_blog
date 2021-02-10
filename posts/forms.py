from django import forms
from tinymce import TinyMCE
from .models import Comment, Post

class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False

class PostForm(forms.ModelForm):
    overview = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 10, 'rows': 5}
        )
    )

    class Meta:
        model = Post
        fields = ('title', 'content', 'overview', 'author', 
            'category', 'image', 'previous_post', 'next_post'
        )

        
class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Type your comment',
        'rows':4
    }))

    class Meta:
        model = Comment
        fields = ['content']



