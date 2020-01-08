from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from learn_django.models import *
from learn_django.forms import productform

# Create your views here.
def index(request):
    page_name = 'HOME PAGE'
    return render(request, 'index.html', {'name':page_name})

def about(request):
    page_name = 'ABOUT PAGE'
    return render(request, 'about.html', {'name':page_name})

def blog(request):
    page_name = 'BLOG PAGE'
    return render(request, 'blog.html', {'name':page_name})

def contact(request):
    page_name = 'CONTACT PAGE'
    return render(request, 'contact.html', {'name':page_name})
    
def product(request):
    page_name = 'PRODUCTS PAGE'
    product_list = Product.objects.all()
    return render(request, 'products.html', {'name':page_name ,'data':product_list})

def add_product(request):
    if request.method == "POST":
        form = productform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = productform()
    return render(request, 'add_product.html', {'form':form})
    
def edit_product(request, id):
    product_item = get_object_or_404(Product, pk=id)
    if request.method == "POST":
        form = productform(request.POST, request.FILES, instance = product_item)
        if form.is_valid():
            form.save()
            return redirect (product)
    else:
        form = productform(instance = product_item)
    return render(request, 'add_product.html', {'form':form})

def visitor(request):
    visitor_list = Visitor.objects.all()
    return render(request, 'visitors.html', {'data':visitor_list})

def add_visitor(request):
    if request.method == "POST":
        new_visitor = Visitor()
        new_visitor.name= request.POST.get('visitor_name')
        new_visitor.age= request.POST.get('age')
        new_visitor.email= request.POST.get('email')
        new_visitor.save()
    return render(request, 'add_visitor.html')