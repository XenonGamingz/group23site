from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Category, Book, Borrower, BorrowRecord, Librarian

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'category', 'publication_year', 'quantity', 'available']


class BorrowerForm(forms.ModelForm):
    class Meta:
        model = Borrower
        fields = ['name', 'student_id', 'contact_number']


class BorrowRecordForm(forms.ModelForm):
    class Meta:
        model = BorrowRecord
        fields = ['borrower', 'book', 'borrow_date', 'return_date', 'is_returned']
        widgets = {
            'borrow_date': forms.DateInput(attrs={'type': 'date'}),
            'return_date': forms.DateInput(attrs={'type': 'date'}),
        }

class LibrarianRegistrationForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            "class": "w-full rounded-lg bg-green-400 text-green-900 placeholder-green-900 px-5 py-3 text-lg focus:outline-none",
            "placeholder": "Username"
        })
    )
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            "class": "w-full rounded-lg bg-green-400 text-green-900 placeholder-green-900 px-5 py-3 text-lg focus:outline-none",
            "placeholder": "First name"
        })
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            "class": "w-full rounded-lg bg-green-400 text-green-900 placeholder-green-900 px-5 py-3 text-lg focus:outline-none",
            "placeholder": "Last name"
        })
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            "class": "w-full rounded-lg bg-green-400 text-green-900 placeholder-green-900 px-5 py-3 text-lg focus:outline-none",
            "placeholder": "Email address"
        })
    )

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            "class": "w-full rounded-lg bg-green-400 text-green-900 placeholder-green-900 px-5 py-3 text-lg focus:outline-none",
            "placeholder": "Create a password (9 characters or longer)"
        })
        self.fields['password2'].widget.attrs.update({
            "class": "w-full rounded-lg bg-green-400 text-green-900 placeholder-green-900 px-5 py-3 text-lg focus:outline-none",
            "placeholder": "Confirm password"
        })
