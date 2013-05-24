from django.shortcuts import render_to_response
from django.template.context import RequestContext

from models import Category
from products.models import Product

def get_categories(request):
    print "GET CAT VIEW CALLED"
    children = Category.objects.filter(parent__isnull=False, published=True)    
    return render_to_response('category/list.html', 
                              {'list' : children},
                              RequestContext(request))

def view_category(request, category):
    print "VIEW CATEGORY VIEW CALLED"
    list = Category.objects.filter(parent__slug__icontains=category)
    if not list:
        list = Category.objects.filter(slug=category)
    
    return render_to_response('category/list.html', 
                              { 'list' : list,
                                'category' : category},
                              RequestContext(request))

def view_product_list(request, category, sub_category):
    print "VIEW PRODUCT LIST VIEW CALLED"
    category = "%s - %s" % (category, sub_category)
    
    products = Product.objects.filter(category__slug=sub_category)
    
    return render_to_response('product/list.html', 
                              { 'list' : products, 
                                'category' : category},
                              RequestContext(request))




















