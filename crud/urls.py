from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import register_librarian


urlpatterns = [
    # Register
    path('register', register_librarian, name='register'),

    # Login
    path('', auth_views.LoginView.as_view(template_name='crud/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # Home Page
    path('home/', views.home, name='home'),

    # Category
    path('categories/', views.category_list, name='category_list'),
    path('categories/add/', views.category_create, name='category_create'),
    path('categories/<int:pk>/edit/', views.category_edit, name='category_edit'),
    path('categories/<int:pk>/delete/', views.category_delete_confirm, name='category_delete'),

    # Books
    path('books/', views.home, name='book_list'),
    path('books/add/', views.book_create, name='book_create'),
    path('books/<int:book_id>/edit/', views.book_edit, name='book_edit'),
    path('books/<int:book_id>/delete/', views.book_delete_confirm, name='book_delete'),

    # Borrowers
    path('borrowers/', views.borrower_list, name='borrower_list'),
    path('borrowers/add/', views.borrower_create, name='borrower_create'),

    # Borrowing
    path('borrow/', views.borrow_list, name='borrow_list'),
    path('borrow/add/', views.borrow_create, name='borrow_create'),
    path('borrows/<int:record_id>/return/', views.return_book, name='return_book'),
]
