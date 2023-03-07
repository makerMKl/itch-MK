from django.db import models
from django.utils import timezone
from book.models import Book

class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    content = models.TextField()
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_time']

    def __str__(self):
        return self.content[:20]