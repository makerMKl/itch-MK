from django.shortcuts import render
from django.http import JsonResponse
from .models import Book, Comment
from django.shortcuts import get_object_or_404

def post_comment(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        content = request.POST.get('content')
        if book_id and content:
            book = Book.objects.get(id=book_id)
            comment = Comment.objects.create(book=book, content=content)

            # Get the latest comments
            comments = Comment.objects.filter(book=book).order_by('-created_time')

            # Prepare the comment data for JSON response
            comment_data = [{'content': comment.content, 'created_time': comment.created_time} for comment in comments]

            # Return the updated comments as JSON response
            return JsonResponse({'success': True, 'message': 'Comment posted successfully!', 'comments': comment_data})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid input!'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method.'})

def get_comments_by_book_id(request, book_id):
    if request.method == 'GET':
        book = Book.objects.get(id=book_id)
        comments = Comment.objects.filter(book=book).order_by('-created_time')
        return JsonResponse({'success': True, 'comments': [{'content': comment.content, 'created_time': comment.created_time} for comment in comments]})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method.'})



