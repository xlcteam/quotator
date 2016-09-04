from datetime import datetime
import json

from django.shortcuts import (render, HttpResponseRedirect, get_object_or_404,
                                    render_to_response)
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User

from .models import Quote
from . import forms

SCHEDULE_FORMAT = '%d.%m.%Y %H:%M'


def project_home(request):
    return render_to_response('quotes/project_home.html',
                              context_instance=RequestContext(request))


def quotes_home(request):
    user_quotes = request.user.quote_set.all().order_by('-created_date')

    return render_to_response('quotes/quotes_home.html',
                              {'quotes': user_quotes},
                              context_instance=RequestContext(request))


def quote_schedule(request):
    quote_pk = request.POST['quote_pk']
    day = request.POST['day']
    month = request.POST['month']
    year = request.POST['year']
    time = request.POST['time']

    done = True
    try:
        obj = Quote.objects.get(pk=quote_pk)
        obj.scheduled = datetime.strptime(
                '{0}.{1}.{2} {3}'.format(day, month, year, time),
                SCHEDULE_FORMAT)
        obj.save()
    except:
        done = False

    result = 'OK' if done else 'FAIL'
    time = obj.scheduled.strftime(SCHEDULE_FORMAT)
    data = {'result': result, 'time': time}
    return HttpResponse(json.dumps(data), content_type='application/json')


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


class QuoteDelete(DeleteView):
    def delete(self, request, *args, **kwargs):
        done = True
        try:
            obj = request.user.quote_set.get(pk=request.POST['quote_pk'])
            obj.delete()
        except:
            done = False

        result = 'OK' if done else 'FAIL'
        data = {'result': result, 'fero': 'taraba'}
        return HttpResponse(json.dumps(data), content_type='application/json')

quote_create = QuoteCreate.as_view()
quote_edit = QuoteEdit.as_view()
quote_delete = QuoteDelete.as_view()
