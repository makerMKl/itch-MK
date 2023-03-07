from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.utils.crypto import get_random_string
from .models import Book
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import BookForm
from comment.models import Comment

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    comments = Comment.objects.filter(book=book).order_by('-created_time')
    #return render(request, 'book/details.html', {'book': book, 'comments': comments})
    return render(request, 'book/details.html', {'book': book})




def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        catIds = request.POST['catIds']
        link = request.POST['link']
        intro = request.POST['intro']
        coverpage = request.FILES['coverpage']

        # Generate a random filename
        filename = get_random_string(length=32)
        # Save the uploaded file to the media folder
        path = default_storage.save(f'books/{filename}.jpg', coverpage)

        # Create a new Book object and save it to the database
        book = Book.objects.create(
            title=title,
            author=author,
            catIds=catIds,
            link=link,
            intro=intro,
            coverpage=f'{filename}.jpg'
        )
        book.save()

        return redirect('/book/list')
    else:
        return render(request, 'add.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})



def book_edit(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == 'GET':
        form = BookForm(instance=book)
        return render(request, 'edit.html', {'form': form, 'book_id': book_id})
    elif request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated successfully.')
            return redirect('/book/list')
        else:
            messages.error(request, 'Error occurred while updating book.')
            return redirect('book_edit', book_id=book_id)

