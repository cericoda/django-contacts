from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseServerError, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from contacts.models import Person
from contacts.forms import PersonCreateForm, PersonUpdateForm, PhoneNumberFormSet, EmailAddressFormSet, WebSiteFormSet, StreetAddressFormSet
from django.core.exceptions import PermissionDenied

def list(request, page=1, template='contacts/person/list.html'):
    """List of all the people.

    :param template: Add a custom template.
    """


    person_list = Person.objects.all()
    paginator = Paginator(person_list, 20)

    try:
        people = paginator.page(page)
    except (EmptyPage, InvalidPage):
        people = paginator.page(paginator.num_pages)

    kwvars = {
        'object_list': people.object_list,
        'has_next': people.has_next(),
        'has_previous': people.has_previous(),
        'has_other_pages': people.has_other_pages(),
        'start_index': people.start_index(),
        'end_index': people.end_index(),
    }

    try:
        kwvars['previous_page_number'] = people.previous_page_number()
    except (EmptyPage, InvalidPage):
        kwvars['previous_page_number'] = None
    try:
        kwvars['next_page_number'] = people.next_page_number()
    except (EmptyPage, InvalidPage):
        kwvars['next_page_number'] = None

    return render_to_response(template, kwvars, RequestContext(request))

def detail(request, pk, slug=None, template='contacts/person/detail.html'):
    """Detail of a person.

    :param template: Add a custom template.
    """


    try:
        person = Person.objects.get(pk__iexact=pk)
    except Person.DoesNotExist:
        raise Http404

    kwvars = {
        'object': person,
    }

    return render_to_response(template, kwvars, RequestContext(request))

def create(request, template='contacts/person/create.html'):
    """Create a person.

    :param template: A custom template.
    """


    user = request.user
    if not user.has_perm('contacts.add_person'):
        raise PermissionDenied

    if request.method == 'POST':
        form = PersonCreateForm(request.POST)

        if form.is_valid():
            p = form.save()
            return HttpResponseRedirect(p.get_absolute_url())
    else:
        form = PersonCreateForm()

    kwvars = {
        'form': form
    }

    return render_to_response(template, kwvars, RequestContext(request))

def update(request, pk, slug=None, template='contacts/person/update.html'):
    """Update a person.

    :param template: A custom template.
    """


    user = request.user
    if not user.has_perm('contacts.change_person'):
        raise PermissionDenied

    try:
        person = Person.objects.get(pk__iexact=pk)
    except person.DoesNotExist:
        raise Http404

    if request.method == 'POST':
        form = PersonUpdateForm(request.POST, instance=person)
        phone_formset = PhoneNumberFormSet(request.POST, instance=person)
        email_formset = EmailAddressFormSet(request.POST, instance=person)
        website_formset = WebSiteFormSet(request.POST, instance=person)
        address_formset = StreetAddressFormSet(request.POST, instance=person)

        if form.is_valid() and phone_formset.is_valid() and \
            email_formset.is_valid() and  \
            website_formset.is_valid() and address_formset.is_valid():
            form.save()
            phone_formset.save()
            email_formset.save()
            website_formset.save()
            address_formset.save()
            return HttpResponseRedirect(person.get_absolute_url())

    else:
        form = PersonUpdateForm(instance=person)
        phone_formset = PhoneNumberFormSet(instance=person)
        email_formset = EmailAddressFormSet(instance=person)
        website_formset = WebSiteFormSet(instance=person)
        address_formset = StreetAddressFormSet(instance=person)


    kwvars = {
        'form': form,
        'phone_formset': phone_formset,
        'email_formset': email_formset,
        'website_formset': website_formset,
        'address_formset': address_formset,
        'object': person,
    }

    return render_to_response(template, RequestContext(request, kwvars))

def delete(request, pk, slug=None, template='contacts/person/delete.html'):
    """Delete a company.

    :param template: A custom template.
    """


    user = request.user
    if not user.has_perm('contacts.delete_person'):
        raise PermissionDenied

    try:
        person = Person.objects.get(pk__iexact=pk)
    except Person.DoesNotExist:
        raise Http404

    if request.method == 'POST':
        new_data = request.POST.copy()
        if new_data['delete_person'] == 'Yes':
            person.delete()
            return HttpResponseRedirect(reverse('contacts_person_list'))
        else:
            return HttpResponseRedirect(person.get_absolute_url())

    kwvars = {
        'object': person
    }

    return render_to_response(template, kwvars, RequestContext(request))