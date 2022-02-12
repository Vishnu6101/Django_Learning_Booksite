from django.shortcuts import redirect, render, get_object_or_404
# from django.http import HttpResponse, Http404
from books.models import Book, Review
# import json

# booksData = open('/home/user/Django Projects/bookstore/books.json').read()

# data = json.loads(booksData)

# Create your views here.


def index(request):
    # context = {'book' : {
    #     'title' : 'Harry Potter and the Prisoner of Azkaban',
    #     'url' : 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.guim.co.uk%2Fimg%2Fstatic%2Fsys-images%2FGuardian%2FPix%2Fpictures%2F2014%2F7%2F30%2F1406718532907%2F396ff814-8791-451b-9214-6a9b86d54142-1360x2040.jpeg%3Fw%3D1200%26q%3D55%26auto%3Dformat%26usm%3D12%26fit%3Dmax%26s%3D6c95eabb2ad2e46429e3e297fca94c58&f=1&nofb=1'
    # }}
    
    dbData = Book.objects.all()
    context = {'books': dbData}
    return render(request, 'books/index.html', context=context)


def show(request, id):
    # singleBook = list()
    # for book in data:
    #     if book['id'] == id:
    #         singleBook = book

    # try:
    #     singleBook = Book.objects.get(pk=id)
    # except Book.DoesNotExist:
    #     raise Http404("Book not Found")

    singleBook = get_object_or_404(Book, pk=id)

    reviews = Review.objects.filter(book=id).order_by('-createdAt')

    context = {'book': singleBook, 'reviews': reviews}
    return render(request, 'books/show.html', context=context)


def review(request, id):
    body = request.POST['review']
    newReview = Review(body=body, book_id=id)
    newReview.save()
    url = '/book/{}'.format(id)
    return redirect(url)