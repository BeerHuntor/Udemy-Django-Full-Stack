from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from catalog.models import Book, Author, BookInstance, Genre,Language
from django.shortcuts import get_object_or_404

# Create your views here.
def CatalogHomeView(request):

    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_avail = BookInstance.objects.filter(status__exact='a').count()
    
    context = {
        'num_books' : num_books,
        'num_instances' : num_instances,
        'num_instances_avail' : num_instances_avail,
    }

    return render(request, 'catalog/index.html', context=context)


class BookCreate(CreateView):
    model = Book
    fields = ['book_title', 'author', 'summary', 'isbn','genre', 'language']
    
    def get_template_names(self):
        return ['catalog/book_form.html']
    
class BookDetail(DetailView):
    model = Book
    fields = "__all__"

    def get_object(self, queryset=None):
        # Retrieve the book based on the slug
        return get_object_or_404(Book, slug=self.kwargs['slug'])
    def get_template_names(self):
        return ['catalog/book_detail.html']