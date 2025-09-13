from django.shortcuts import render,redirect
from favorit_books_app.models import *
import bcrypt
from django.contrib import messages
def index(request):
    return render(request,'index.html')
def create_user(request):
    if request.method=='POST':
        errors=Users.objects.user_validator(request.POST)
       
        if len(errors)>0 :
            for key,value in errors.items():
                messages.error(request,value)
            return redirect('index')
        else:
            password = request.POST.get('password')
            pw_hash=bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()

            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            email=request.POST['email']
            user= Users.objects.create(first_name=first_name,last_name=last_name,email=email,password=pw_hash)
            request.session['first_name']=request.POST['first_name']
            request.session['user_id']=user.id
            messages.success(request,"Successfully create User")
            return redirect('index')
    return redirect('index')

def log_in(request):
    if request.method== 'POST':
        email=request.POST['email']
        password=request.POST['password']
        user=Users.objects.filter(email=email).first()
        if user and bcrypt.checkpw(password.encode(),user.password.encode()):
            request.session['first_name']=user.first_name
            request.session['user_id']=user.id
            messages.success(request,"Successfully logged in")
            return redirect('books')
        else:
            messages.error(request,"Invalid email or password")
            return redirect('index')
    return redirect('index')
def fav_book(request):
     if 'first_name' not in request.session:
        return redirect('index')
     return render(request,"favorit_books.html")
def logout(request):
    request.session.flush()
    list(messages.get_messages(request))
    messages.success(request,"You have been logged out")
    return redirect('index')
def add_book(request):
    if request.method=='POST':
        errors=books.objects.book_validator(request.POST)
       
        if len(errors)>0 :
            for key,value in errors.items():
                messages.error(request,value)
            return redirect('books')
        else:
            title = request.POST.get('title')
            desc= request.POST.get('desc')
            user=Users.objects.get(first_name=request.session['first_name'])
            uploded_by=user
            book=books.objects.create(title=title,desc=desc,uploded_by=uploded_by)
            book.liked_by.add(user)
            messages.success(request,"Successfully Add Book")
            return redirect('books')
    return redirect('books')


def fav_book(request):
    if 'user_id' not in request.session:
        return redirect('index')
    user=Users.objects.get(id=request.session['user_id'])
    all_books=books.objects.all()
    user_fav_books = list(user.liked_books.values_list('id', flat=True))
    context={
        "user":user,
        "all_books":all_books,
        "user_fav_books": user_fav_books
    }
    return render(request,"favorit_books.html",context)


def book_detail(request,book_id):
    if 'user_id' not in request.session:
        return redirect('index')
    
    book=books.objects.get(id=book_id)
    user= Users.objects.get(id=request.session['user_id']) 
    is_favorite=user in book.liked_by.all()

    context={
        "book":book,
        "user":user,
        "is_favorite":is_favorite,
        "users_who_like":book.liked_by.all()
    }
    return render(request,"book_details.html",context)
    
def add_to_favorite(request,book_id):
    if 'user_id' not in request.session:
        return redirect('index')

    user = Users.objects.get(id=request.session['user_id'])
    book = books.objects.get(id=book_id)

   
    if user not in book.liked_by.all():
        book.liked_by.add(user)
        messages.success(request, f"{book.title} has been added to your favorites")
    else:
        messages.info(request, f"{book.title} is already in your favorites")
    return redirect('book_detail', book_id=book.id)
    




def unfavorite_book(request, book_id):
    if 'user_id' not in request.session:
        return redirect('index')

    user = Users.objects.get(id=request.session['user_id'])
    book = books.objects.get(id=book_id)
    book.liked_by.remove(user)
    return redirect('book_detail', book_id=book.id)

def update_book(request, book_id):
    if 'user_id' not in request.session:
        return redirect('index')

    book = books.objects.get(id=book_id)
    if book.uploded_by.id != request.session['user_id']:
        messages.error(request, "You are not allowed to edit this book")
        return redirect('books')

    if request.method == 'POST':
        errors = books.objects.book_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/books/{book_id}')

        book.title = request.POST['title']
        book.desc = request.POST['desc']
        book.save()
        messages.success(request, "Book updated successfully")
    return redirect('book_detail', book_id=book.id)
def delete_book(request, book_id):
    if 'user_id' not in request.session:
        return redirect('index')

    book = books.objects.get(id=book_id)
    if book.uploded_by.id == request.session['user_id']:
        book.delete()
        messages.success(request, "Book deleted successfully")
    else:
        messages.error(request, "You cannot delete this book")
    return redirect('books')

def my_favorites(request):
    if 'user_id' not in request.session:
        return redirect('index')
    
    user = Users.objects.get(id=request.session['user_id'])
    fav_books = user.liked_books.all()
    
    context = {
        "user": user,
        "fav_books": fav_books
    }
    return render(request, "my_favorit.html", context)
# Create your views here.
