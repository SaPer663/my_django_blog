from django import forms
from django.forms import TextInput, Textarea
from .models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        widgets = {
            'name' : TextInput(attrs={'type' : 'text', 
                                     'class' : 'form-control',
                                     'id' : 'name',
                                     'placeholder' : 'Enter Name',
                                     'onfocus' : "this.placeholder = ''",
                                     'onblur' : "this.placeholder = 'Enter Name'"}),
            'email' : TextInput(attrs={'type' : 'email',
                                       'class' : 'form-control',
                                       'id' : 'email',
                                       'placeholder' : 'Enter email address',
                                       'onfocus' : 'this.placeholder = ""',
                                       'onblur' : 'this.placeholder = "Enter email address"'}),
            'body' : Textarea(attrs={'class' : 'form-control mb-10',
                                     'rows' : '5',
                                     'name' : 'message',
                                     'placeholder' : 'Messege',
                                     'onfocus' : 'this.placeholder = ""',
                                     'onblur' : 'this.placeholder = "Messege"',
                                     'required' : ""})                                  
        }
        