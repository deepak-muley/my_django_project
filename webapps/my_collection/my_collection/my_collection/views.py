from django.shortcuts import render_to_response, get_object_or_404
from django.template import Context, loader, RequestContext
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def landing_page(request):
    return render_to_response('landing.html', RequestContext(request))

def find_your_location(request):
    return render_to_response('find_your_location.html', RequestContext(request))

@login_required
def about(request):
    return render_to_response('about.html', RequestContext(request))

@login_required
def contact(request):
    return render_to_response('contact.html', RequestContext(request))

@login_required
def scratch_pad(request):
    return render_to_response('html_scratch_pad.html', RequestContext(request))

@login_required
def scratch_pad2(request):
    return render_to_response('html_scratch_pad2.html', RequestContext(request))

@login_required
def user_home(request, user_name=''):
    context = {
               'username': user_name
               }
    return render_to_response('user_home.html', context, context_instance=RequestContext(request))