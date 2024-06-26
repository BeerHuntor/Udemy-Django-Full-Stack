from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from django.template.defaultfilters import slugify

import uuid
# Create your models here.
class Genre(models.Model):
    # model representing a book genre
    name = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.name}'
    
class Language(models.Model):
    # model representing language of the book
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'
    
class Book(models.Model):
    # model representing a book. 
    book_title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True) # This means if someone somehow accidently deletes the author, the book still exists, and author just returns NULL
    publish_date = models.DateField(auto_now=False, auto_now_add=True)
    summary = models.TextField(max_length=1000)
    isbn = models.CharField('ISBN', max_length=13, unique=True)
    genre = models.ManyToManyField(Genre) # book can have a list of potential genres
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    
    def save(self, *args, **kwargs):
        #Generate slug based on title
        self.slug = slugify(self.book_title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.book_title}'
    
    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'slug': self.slug})


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)

    class Meta: 
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('author_detail', kwargs={'pk': self.pk})
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(auto_now=False, auto_now_add=False, null=True)
    borrowed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    LOAN_STATUS = [
        ('m', 'Maintenece'),
        ('o', 'On Loan'),
        ('a', 'Available'),
        ('r', 'Reserved')    
    ]

    status = models.CharField(max_length=1,choices=LOAN_STATUS, blank=True, default='m')

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id} ({self.book.book_title})'
    
