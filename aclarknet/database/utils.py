from decimal import Decimal
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from import_export import widgets


class DecimalWidget(widgets.Widget):
    """
    Custom Django Import/Export Widget to import decimal values from strings.
    (Django Import/Export's DecimalWidget does not convert strings.)
    """

    def clean(self, value):
        if value:
            return Decimal(value.replace(',', ''))
        else:
            return Decimal(0)


def class_name_pk(self):
    """
    Django Admin object names based on class and pk, e.g.:

        client-1
        client-2
        client-3
    """
    return '-'.join([self.__class__.__name__.lower(), str(self.pk)])


def edit(request, form_model, model, url_name, template, pk=None):
    context = {}

    if pk is None:
        form = form_model()
    else:
        obj = get_object_or_404(model, pk=pk)
        form = form_model(instance=obj)

    if request.method == 'POST':

        if pk is None:
            form = form_model(request.POST)
        else:
            active = request.POST.get('active')
            if active == 'on' or active == 'off':
                if active == 'on':
                    obj.active = True
                else:
                    obj.active = False
                obj.save()
                return HttpResponseRedirect(reverse(url_name))

            form = form_model(request.POST, instance=obj)

        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect(reverse(url_name))

    context['form'] = form
    return render(request, template, context)


def entries_total(queryset):
    """
    Add entries for estimates & invoices
    """
    entries = {}
    running_total = 0
    for entry in queryset:
        entries[entry] = {}
        entries[entry]['notes'] = entry.notes
        hours = entry.hours
        entries[entry]['hours'] = hours
        if entry.task:
            rate = entry.task.rate
            entries[entry]['rate'] = rate
            total = float(rate) * float(hours.total_seconds() / 60)
            entries[entry]['total'] = total
            running_total += total
    return entries, running_total


def paginate(items, page):
    """
    Django Paginator, based on:

        https://docs.djangoproject.com/en/1.9/topics/pagination/

    but show last page first, along with template:

        <div class="pagination">
            <span class="step-links">
                {% if items.has_next %}
                    <a href="?page={{ items.next_page_number }}">
                        <i class="fa fa-arrow-left"></i></a>
                {% endif %}
                <span class="current">
                    {{ items.number }} of {{ items.paginator.num_pages }}
                </span>
                {% if items.has_previous %}
                    <a href="?page={{ items.previous_page_number }}">
                        <i class="fa fa-arrow-right"></i></a>
                {% endif %}
            </span>
        </div>
    """
    paginator = Paginator(items, 10, orphans=5)  # Show 10 per page
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver last page.
        items = paginator.page(paginator.num_pages)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver first page of results.
        items = paginator.page(1)
    return items
