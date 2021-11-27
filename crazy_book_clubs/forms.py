from django import forms

from .models import Book
from .models import Review

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'year_published']
        labels = {'name': ''}

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['my_review', 'unfinished' ]
        labels = {'my_review': 'Review:'}
        widgets = {'my_review': forms.Textarea(attrs={'cols':80})}
        
        


