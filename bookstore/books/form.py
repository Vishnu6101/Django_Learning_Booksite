from django import forms
from books.models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['body']
        widgets = {'body' : forms.Textarea(attrs={
            'class' : "p-2 my-2 w-full rounded-lg border border-blue-500",
            'placeholder' : 'Write a review',
            'cols' : 30,
            'rows' : 5
        })}
        labels = {
            'body' : ('')
        }