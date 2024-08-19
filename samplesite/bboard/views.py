from .models import Book, Author,Reading
from django.shortcuts import render, get_object_or_404
from datetime import date

from django.shortcuts import render, get_object_or_404
from .models import Author

def books_by_author(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    books = Book.objects.filter(authors=author).prefetch_related('authors')
    return render(request, 'books_by_author.html', {'author': author, 'books': books})

def readers_for_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    readers = Reading.objects.filter(book=book).select_related('reader')
    return render(request, 'readers_for_book.html', {'book': book, 'readers': readers})

def recent_readers_for_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    recent_readings = Reading.objects.filter(book=book, start_date__gt=date(2024, 8, 1)).select_related('reader')
    return render(request, 'recent_readers_for_book.html', {'book': book, 'recent_readings': recent_readings})

