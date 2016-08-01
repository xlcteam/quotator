from django.shortcuts import render_to_response
from django.template import RequestContext


def project_home(request):
    return render_to_response('quotes/project_home.html',
                              context_instance=RequestContext(request))


