from .models import Comments
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'id': 'inputLogin',
                                                              'placeholder': 'Логін'
                                                               }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'type': 'password',
                                                                  'class': 'form-control',
                                                                  'id': 'inputPassword',
                                                                  'placeholder': 'Пароль'
                                                                   }))
    


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
