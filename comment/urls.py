from django.urls import path
from . import views

urlpatterns = [
    path('post_comment/', views.post_comment, name='post_comment'),
    path('get_comments_by_book_id/<int:book_id>/', views.get_comments_by_book_id, name='get_comments_by_book_id'),
]
