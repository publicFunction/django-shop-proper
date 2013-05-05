from django.shortcuts import render_to_response
from django.template.context import RequestContext

from models import Category
from products.models import Product

def get_categories(request):
    print "GET CAT CALLED"
    children = Category.objects.filter(parent__isnull=False, published=True)    
    return render_to_response('category/list.html', 
                              {'list' : children},
                              RequestContext(request))

def view_category(request, category):
    print "VIEW CALLED"
    if "-" in category:
        cat = category.split('-')
        cat = '%s %s' % (cat[0], cat[1])
        print cat
    else:
        cat = category    
    list = Category.objects.filter(parent__name__icontains=cat)
    if not list:
        list = Category.objects.filter(name__icontains=cat)
        
    return render_to_response('category/list.html', 
                              { 'list' : list},
                              RequestContext(request))

def view_product_list(request, category, sub_category):
    print "VIEW PRODUCT LIST"
    if "-" in sub_category:
        cat = sub_category.split('-')
        cat = '%s %s' % (cat[0], cat[1])
        print cat
    
    return render_to_response('product/list.html', 
                              { 'list' : list },
                              RequestContext(request))

def createMenu():
    parents = Category.objects.filter(parent__isnull=True, published=True)
    return parents