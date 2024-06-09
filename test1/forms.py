from django import forms
from .models import Post, Category, Comment

#hard coded version
# choices = [('coding', 'coding'), ('sports', 'sports'), ('something_else', 'something_else')]
choices = Category.objects.all().values_list('name', 'name')

choices_list = []

for item in choices:
    choices_list.append(item)



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'title_tag', 'author', 'category', 'body', 'snippet', 'header_image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'placeholder': 'user_name', 'id': 'user', 'type': 'hidden'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            #commented out is the hardcoded version
            # 'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choices_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),

        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'title_tag', 'body', 'snippet']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),

        }

        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'body' :  forms.Textarea(attrs={'class': 'form-contol'}),
        }