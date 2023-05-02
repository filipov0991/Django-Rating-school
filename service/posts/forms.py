from django import forms
from .models import Post, Comment, Rating

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['school_name', 'country', 'city', 'website', 'your_email']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class RatingForm(forms.ModelForm):
    rating = forms.IntegerField(
        label='Rating',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5})
    )

    class Meta:
        model = Rating
        fields = ['rating']


class SearchForm(forms.Form): 
    query = forms.CharField()