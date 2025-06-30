from django import forms
from .models import NewsArticle,Comment,UserProfile

class NewsArticleForm(forms.ModelForm):
    class Meta:
        model = NewsArticle
        fields = ['title', 'content','category']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'نظر خود را بنویسید...'}),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'avatar']