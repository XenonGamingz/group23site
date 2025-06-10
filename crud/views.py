from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Book, Borrower, BorrowRecord
from .forms import CategoryForm, BookForm, BorrowerForm, BorrowRecordForm, Librarian
from django.utils import timezone
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import LibrarianRegistrationForm
from django.db.models import Q
from django.contrib import messages

def register_librarian(request):
    if request.method == 'POST':
        form = LibrarianRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Librarian registered successfully!')
            Librarian.objects.create(user=user)
            login(request, user)  # Optional: log the user in right after registration
            return redirect('login')  # or your desired redirect URL
    else:
        form = LibrarianRegistrationForm()

    return render(request, 'crud/register.html', {'form': form})

# Home / Dashboard

# @login_required
def home(request):
    query = request.GET.get('q', '')
    selected_category = request.GET.get('category', '')
    
    books = Book.objects.all()

    if query:
        books = books.filter(title__icontains=query)

    if selected_category:
        books = books.filter(category_id=selected_category)

    categories = Category.objects.all()

    return render(request, 'crud/home.html', {
        'books': books,
        'categories': categories,
        'query': query,
        'selected_category': selected_category,
    })



# CATEGORY VIEWS
# @login_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'crud/category_list.html', {'categories': categories})

# @login_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category added successfully!')
            return redirect('home')
    else:
        form = CategoryForm()
    return render(request, 'crud/category_form.html', {'form': form})


# BOOK VIEWS
# @login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'crud/book_list.html', {'books': books})

# @login_required
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book added successfully!')
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'crud/book_form.html', {'form': form})


# BORROWER VIEWS
# @login_required
def borrower_list(request):
    borrowers = Borrower.objects.all()
    return render(request, 'crud/borrower_list.html', {'borrowers': borrowers})

# @login_required
def borrower_create(request):
    if request.method == 'POST':
        form = BorrowerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Borrower added successfully!')
            return redirect('borrower_list')
    else:
        form = BorrowerForm()
    return render(request, 'crud/borrower_form.html', {'form': form})


# BORROW RECORD VIEWS
# @login_required
def borrow_list(request):
    borrow_records = BorrowRecord.objects.select_related('borrower', 'book').all()
    return render(request, 'crud/borrow_list.html', {'borrow_records': borrow_records})


# @login_required
def borrow_create(request):
    if request.method == 'POST':
        form = BorrowRecordForm(request.POST)
        if form.is_valid():
            book = form.cleaned_data['book']
            if book.available > 0:
                record = form.save()
                # Update book availability
                book.available -= 1
                book.save()
                messages.success(request, f"Book '{book.title}' successfully lent!")
                return redirect('borrow_list')
            else:
                form.add_error('book', 'Selected book is not available for lending.')
    else:
        form = BorrowRecordForm()
    return render(request, 'crud/borrow_form.html', {'form': form})

# @login_required
def return_book(request, record_id):
    record = get_object_or_404(BorrowRecord, id=record_id)
    if not record.is_returned:
        record.is_returned = True
        record.return_date = timezone.now()
        record.save()
        # Update book availability
        book = record.book
        book.available += 1
        book.save()
    return redirect('borrow_list')
