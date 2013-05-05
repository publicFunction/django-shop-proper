

def view_products_list(request, category, sub_category):
    products = None
    print "PRODUCT LIST VIEW CALLED"
    return render_to_response('product/list.html', 
                              {'list' : products},
                              RequestContext(request))
