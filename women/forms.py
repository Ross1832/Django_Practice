from django import forms
from .models import Women, Category


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, label='Header', widget=forms.TextInput(attrs={'class': 'form-input'}))
    slug = forms.SlugField(max_length=255)
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    is_published = forms.BooleanField(label='Published', required=False, initial=True)
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Category', empty_label="Choose the category")

