from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def index(request):
    contacts = Contact.objects.all()
    search_input = request.GET.get('search-area')
    if search_input:
        contacts = Contact.objects.filter(full_name__icontains=search_input)
    else:
        contacts = Contact.objects.all()
        search_input = ''
    return render(request, 'index.html', {'contacts':contacts, 'search_input':search_input})

def addContact(request):
    if request.method == 'POST':
        new_contact = Contact(
            full_name=request.POST.get('fullname'),
            relationship=request.POST.get('relationship'),
            email=request.POST.get('email'),
            phone_number=request.POST.get('phone'),
            address=request.POST.get('address'),
        )
        new_contact.save()
        return redirect('/')
    return render(request, 'new.html')

def contactProfile(request, pk):
    contact = Contact.objects.get(id=pk)
    return render(request, 'contact-profile.html', {"contact": contact})

def editContact(request, pk):
    contact = Contact.objects.get(id=pk)
    if request.method == 'POST':
        contact.full_name=request.POST.get('fullname')
        contact.relationship=request.POST.get('relationship')
        contact.email=request.POST.get('email')
        contact.phone_number=request.POST.get('phone')
        contact.address=request.POST.get('address')
        contact.save()
        return redirect(f'/profile/{contact.id}')
    
    return render(request, 'edit.html',  {"contact": contact})


def deleteContact(request, pk):
    contact = Contact.objects.get(id=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('/')
    return render(request, 'delete.html', {"contact": contact})