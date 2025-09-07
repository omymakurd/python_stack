from django.shortcuts import render,redirect
from .models import Books,Authors
def index(request):
    context={
        "books":Books.objects.all()
    }
    return render(request,"index.html",context)
def add_book(request):
    if request.method=='POST':
       title=request.POST['title'] 
       desc=request.POST['desc']
       Books.objects.create(title=title,desc=desc)
       return redirect('/')
    return redirect('/')

def show_book(request,id):
    book=Books.objects.get(id=id)
    authors=Authors.objects.exclude(id__in=book.authors.all())
    if request.method=="POST":
        author_id=request.POST['author']
        author=Authors.objects.get(id=author_id)
        book.authors.add(author)
        return redirect(f'/books/{id}/')
    context={
        "book":book,
        "authors":authors
    }
    return render(request,"books-details.html",context)
def show_authors(request):
    context={
        "authors":Authors.objects.all()
    }
    return render(request,'authors.html',context)
def add_author(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        notes=request.POST['notes']
        Authors.objects.create(first_name=first_name,last_name=last_name,notes=notes)
        return redirect('/authors/')
    return redirect('/authors/')
def show_author_book(request,id):
    author=Authors.objects.get(id=id)
    books=Books.objects.exclude(id__in=author.books.all())
    if request.method=='POST':
        book_id=request.POST['book']
        book=Books.objects.get(id=book_id)
        author.books.add(book)
        return redirect(f'/authors/{id}/')
    context={
        "author":author,
        "books":books
    }
    return render(request,'authors-details.html',context)



# Create your views here.
