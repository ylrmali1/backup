from django.shortcuts import render
from main.models import Product, Blog


def index(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs,
    }
    return render(request, 'main/index.html', context)


def contact(request):
    return render(request, 'main/contact.html')


def product(request):
    products = Product.objects.all()
    return render(request, 'main/product.html', context={'products': products})


def product_detail(request,pk):
    product = Product.objects.get(id=pk)
    return render(request, 'main/product-details.html', context={'product': product})


def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'main/blog.html', context={'blogs': blogs})


def blog_detail(request,pk):
    blog = Blog.objects.get(id=pk)
    return render(request, 'main/blog-details.html', context={'blog': blog})
