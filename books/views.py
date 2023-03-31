from django.shortcuts import render, redirect

from books.models import Book


def index(request):
    return redirect('books')


def books_view(request):

    all_books = Book.objects.all()
    template = 'books/books_list.html'
    context = {'books': all_books}

    return render(request, template, context)

# По условию задания не совсем понял, на одинаковую дату выводить первую книгу из списка или все книги. Сделал и так и так..


# def book_info(request, date):
#
#     book = Book.objects.filter(pub_date=date).first()
#     book_next_date = Book.objects.filter(pub_date__lt=date).values("pub_date").first()
#     book_previous_date = Book.objects.filter(pub_date__gt=date).values("pub_date").first()
#     context = {'book': book,
#                'next_page': book_next_date,
#                'previous_page': book_previous_date, }
#     template = 'books/book_info.html'
#
#     return render(request, template, context)

def book_info(request, date):

    books = Book.objects.filter(pub_date=date)
    book_next_date = Book.objects.filter(pub_date__lt=date).values("pub_date").first()
    book_previous_date = Book.objects.filter(pub_date__gt=date).values("pub_date").first()
    context = {'books': books,
               'next_page': book_next_date,
               'previous_page': book_previous_date,}
    template = 'books/book_info2.html'

    return render(request, template, context)