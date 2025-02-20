from .models import Comments
from django import forms


class CommentForm(forms.Form):
    name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                        'id': 'nameInput'
                                                                        }))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'id': 'exampleInputEmail',
                                                           'area-describedby': 'emailHelp'
                                                           }))

    comment = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control',
                                                                           'id': 'comments',
                                                                           'rows': '3'}))


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                        'id': 'nameInput'
                                                                        }))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'id': 'exampleInputEmail',
                                                           'area-describedby': 'emailHelp'
                                                           }))
    to = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                        'id': 'emailTo'}))
    comment = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control',
                                                                           'id': 'comments',
                                                                           'rows': '3'}))
