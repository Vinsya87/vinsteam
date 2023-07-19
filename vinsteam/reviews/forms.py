from django import forms
from django.core.exceptions import ValidationError

from .models import Review


class ReviewForm(forms.ModelForm):

    def clean_name(self):
        name = self.cleaned_data['name']
        if not all(char.isalpha() or char.isspace() for char in name):
            raise ValidationError('Имя не должно содержать цифр или специальных символов.')
        return name

    class Meta:
        model = Review
        fields = ('name', 'email', 'phone', 'text')
        labels = {
            'name': '',
            'email': '',
            'phone': '',
            'text': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form_control', 'placeholder': 'Имя'}),
            'email': forms.EmailInput(attrs={'class': 'form_control', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form_control', 'placeholder': 'Телефон'}),
            'text': forms.Textarea(attrs={'class': 'form_control', 'placeholder': 'Ваш отзыв'}),
}

