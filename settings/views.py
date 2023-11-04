from django.shortcuts import render

from products.models import Brand , Product , Review

def home(request):
    brands = Brand.objects.all()[:10]     # [:10] يعني احضار اول 10 براندات
    sale_products = Product.objects.filter(flag='Sale')[:10]
    feature_products = Product.objects.filter(flag='Feature')[:5]
    new_products = Product.objects.filter(flag='New')[:10]
    reviews= Review.objects.all()[:6]

    return render(request,'settings/home.html',{
        'brands': brands,
        'sale_products': sale_products,
        'feature_products': feature_products,
        'new_products': new_products, 
        'reviews': reviews 
    })