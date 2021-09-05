from django.shortcuts import render, redirect
from owner import forms
from owner import models

# Create your views here.


def home(request):
    return render(request, 'index.html')


def sign_up(request):
    form = forms.SignUpForm
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        return redirect('signin')
    return render(request, 'sign_up.html', {'form': form})


def sign_in(request):
    form = forms.SignInForm
    if request.method == 'POST':
        form = forms.SignInForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect('addbook')
    return render(request, 'sign_in.html', {'form': form})


# def book_create_modelform(request):
#     form = forms.BookForm
#     if request.method == 'POST':
#         form = forms.BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('listbook')
#     return render(request, 'book_add.html', {'form': form})


def book_update_modelform(request, id):
    book = models.Book.objects.get(id=id)
    form = forms.BookEditForm(instance=book)
    if request.method == 'POST':
        form = forms.BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
        return redirect('listbook')
    return render(request, 'book_add.html', {'form': form})


# 8000/owner/books/add/
def book_create(request):
    if request.method == 'GET':
        return render(request, "book_add.html")
    elif request.method == 'POST':
        print(request.POST)
        # book_name = request.POST['book_name']
        book_name = request.POST.get('book_name')
        author = request.POST.get('author')
        price = request.POST.get('price')
        copies = request.POST.get('copies')

        # ORM - (Object Relational Mapper) Query
        book = models.Book(book_name=book_name, author=author, price=price, copies=copies)
        book.save()
        return redirect('listbook')
    return render(request, 'book_add.html')


# 8000/owner/books/
def book_list(request):
    # fetch all record
    books = models.Book.objects.all()
    # search by book_name
    if request.method == 'POST':
        book_name = request.POST.get('book_name')
        books = models.Book.objects.filter(book_name__contains=book_name)
    return render(request, 'book_list.html', {'books': books})


# 8000/owner/books/{id}/
def book_view(request, id):
    # fetch a specific record
    book = models.Book.objects.get(id=id)
    return render(request, 'book_view.html', {'book': book})


# 8000/owner/books/change/{id}/
def book_update(request, id):
    # update a specific record
    book = models.Book.objects.get(id=id)
    # data = {'book_name': book.book_name, 'author': book.author, 'price': book.price, 'copies': book.copies}
    # form = forms.BookUpdateForm(initial=data)
    # if form.is_valid():
    if request.method == 'POST':
        book_name = request.POST.get('book_name')
        author = request.POST.get('author')
        price = request.POST.get('price')
        copies = request.POST.get('copies')

        book.book_name = book_name
        book.author = author
        book.price = price
        book.copies = copies
        book.save()
        return redirect('listbook')
    return render(request, 'book_edit.html', {'book': book})


# 8000/owner/books/remove/{id}/
def book_remove(request, id):
    # delete a specific record
    book = models.Book.objects.get(id=id)
    book.delete()
    return redirect('listbook')



