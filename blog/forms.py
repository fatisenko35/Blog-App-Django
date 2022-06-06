
from django import forms
from .models import BlogModel, CommentModel
class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ['title', 'body', 'image_url', 'author']
        widgets = {
        'title' : forms.TextInput(attrs={'class': 'form-control'}),
        'pub_date' : forms.DateTimeInput(attrs={'class': 'form-control'}),
        'body' : forms.Textarea(attrs={'class': 'form-control', 'rows': '5', 'cols':'5'}),
        'image_url' : forms.TextInput(attrs={'class': 'form-control'}),
        'author' : forms.Select(attrs={'class': 'form-control', 'id': 'ad', 'style' : 'display: none'})
       
}

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['comment', 'author']
        widgets = {
        'comment' : forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'cols':'3'}),
        'author' : forms.Select(attrs={'class': 'form-control', 'id': 'ad', 'style' : 'display: none'})
        }
