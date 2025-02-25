from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from contact.models import Contact


def index(request):
    contacts = Contact.objects \
                      .filter(show=True) \
                      .order_by('-id')  # to slice use [:10]

    paginator = Paginator(contacts, 10)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # print(contacts.query)
    context = {
        'page_obj': page_obj,
        'site_title': 'Contatos - '
    }
    return render(
        request,
        'contact/index.html',
        context=context
    )


def search(request):
    search_value = request.GET.get('q', '').strip()
    if search_value == '':
        return redirect('contact:index')

    contacts = Contact.objects \
            .filter(show=True) \
            .filter(
                Q(first_name__icontains=search_value) |
                Q(last_name__icontains=search_value)
            ) \
            .order_by('first_name')  # to slice use [:10]

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Search - '
    }
    return render(
        request,
        'contact/index.html',
        context=context
    )


def contact(request, contact_id):
    # single_contact = Contact.objects.filter(pk=contact_id).first()
    single_contact = get_object_or_404(Contact, pk=contact_id)
    contact_name = f'{single_contact.first_name} {single_contact.last_name} - '
    context = {
        'contact': single_contact,
        'site_title': contact_name
    }
    return render(
        request,
        'contact/contact.html',
        context=context
    )
