from django import forms

class BlogSearchForm(forms.Form):
    search_query = forms.CharField(
        label='Search Our Blog',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm placeholder-dark border-end-0'}),
    )