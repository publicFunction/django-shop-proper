from django.shortcuts import render_to_response
from django.template.context import RequestContext

def index(request):
    print "SHOP INDEX"
    return render_to_response('theshop/index.html', 
                              {},
                              RequestContext(request))
    
