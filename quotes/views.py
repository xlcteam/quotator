from datetime import datetime

from django.shortcuts import (render, HttpResponseRedirect, get_object_or_404,
                                    render_to_response)
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.http import Http404
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User

from .models import Quote
from . import forms


def project_home(request):
    return render_to_response('quotes/project_home.html',
                              context_instance=RequestContext(request))


def quotes_home(request):
    user_quotes = request.user.quote_set.all().order_by('-created_date')

    return render_to_response('quotes/quotes_home.html',
                              {'quotes': user_quotes},
                              context_instance=RequestContext(request))


class QuoteCreate(CreateView):
    template_name = 'quotes/quote_create.html'
    form_class = forms.QuoteCreateForm

    def form_valid(self, form):
        form.instance.created_date = datetime.now()
        form.instance.user = self.request.user
        return super(QuoteCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('quotes_home')


class QuoteEdit(UpdateView):
    template_name = 'quotes/quote_create.html'
    form_class = forms.QuoteCreateForm

    def get_object(self, queryset=None):
        return self.request.user.quote_set.get(pk=self.kwargs['quote_id'])

    def get_success_url(self):
        return reverse('quotes_home')


quote_create = QuoteCreate.as_view()
quote_edit = QuoteEdit.as_view()
