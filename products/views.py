from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from .models import Product , Brand , Review
from django.db.models import Q , Value , F
from django.db.models.aggregates import Count,Min,Max,Avg,Sum
from django.views.decorators.cache import cache_page
from django.utils import translation


def brand_list(request):
    data = Brand.objects.all()  #query --> method--> change data main query
    return render(request,'html',{'brands':data}) #{'brands':data} --> context --> method(extra data) , html = template

@cache_page(60 * 1)
def mydebug(request):
    # data = Product.objects.filter(price__gte=100)
    # data = Product.objects.filter(price__lte=100)
    # data = Product.objects.filter(price__range=(20,22))

    # data = Product.objects.filter(brand__id__gt = 50)

    # data = Product.objects.filter(name__contains = 'Hill')
    # data = Product.objects.filter(name__startswith = 'Denise')
    # data = Product.objects.filter(name__endswith = 'Hill')
    # data = Product.objects.filter(name__isnull = True)

    # data = Product.objects.filter(price__gte =80 , name__endswith = 'Hill')

    # data = Product.objects.filter(
    #     Q(price__gte = 99) |
    #     Q(name__endswith = 'Hill')
    # )

    # data = Product.objects.order_by('price')
    # data = Product.objects.order_by('-price')
    # data = Product.objects.order_by('name','-price')
    # data = Product.objects.filter(flag='New').order_by('-price')

    # data = Product.objects.order_by('price')[0]  [-1]
    # data = Product.objects.earliest('price')
    # data = Product.objects.latest('price')
    # data = Product.objects.all()[:10]

    # data = Product.objects.values('name','flag')
    # data = Product.objects.only('name','flag')
    # data = Product.objects.defer('quantity')

    # data = Product.objects.select_related('brand').all()   # foreignkey , one-to-one
    # data = Product.objects.prefetch_related('brand').all()   # many to many

    # aggregation : min max sum avg count
    # data = Product.objects.aggregate(myavg = Avg('price'))
    # data = Product.objects.aggregate(Count('quantity'))
    # data = Product.objects.aggregate(Count('id'))

    # data = Product.objects.aggregate(Sum('quantity'))

    # data = Product.objects.aggregate(Min('price'))


    # data = Product.objects.annotate(price_with_tax=F('price')*1.25)

    data = Product.objects.all()
    return render(request, 'products/debug.html',{'data':data})


class ProductList(generic.ListView):
    model = Product
    paginate_by = 50

    def get_queryset(self):
        queryset = Product.objects.all()
        if 'HTTP_ACCEPT_LANGUAGE' in self.request.META:
            lang = self.request.META['HTTP_ACCEPT_LANGUAGE']
            translation.activate(lang)
        return queryset

class ProductDetail(generic.DetailView):
    model = Product

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.filter(product=self.get_object())
        return context

class BrandList(generic.ListView):
    model = Brand
    paginate_by = 50

class BrandDetail(generic.ListView):
    model = Product
    template_name = 'products/brand_detail.html'

    #override main query to gett product for brand coming from url
    def get_queryset(self):
        brand = Brand.objects.get(slug=self.kwargs['slug'])
        queryset = super().get_queryset().filter(brand=brand)
        return queryset
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.get(slug=self.kwargs['slug'])
        return context
    