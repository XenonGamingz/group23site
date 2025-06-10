from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Category model for organizing books
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# Book model to store book information
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=14, unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    publication_year = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default=1)
    available = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.title} by {self.author}"


# Borrower model with student ID instead of email
class Borrower(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20, unique=True)
    contact_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} ({self.student_id})"


# BorrowRecord model to track borrowing activities
class BorrowRecord(models.Model):
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(default=timezone.now)
    return_date = models.DateField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.borrower.name} - {self.book.title}"
    

# Add Librarian
class Librarian(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.username or self.user.get_full_name() or self.user.username
