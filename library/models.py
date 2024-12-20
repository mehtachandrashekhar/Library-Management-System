from django.db import models

class Author(models.Model):
    objects = None
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    objects = None
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    isbn = models.CharField(unique=True, max_length=13)
    available_copies = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class BorrowRecord(models.Model):
    objects = None
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_by = models.CharField(max_length=255)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.book.title} borrowed by {self.borrowed_by}"
