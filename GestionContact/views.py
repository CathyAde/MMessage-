
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Contact
from .forms import ContactForm

@login_required(login_url='login')
def gerer_contact(request):
    contacts = Contact.objects.filter(owner=request.user)
    return render(request, 'gestion_contact.html', {'contacts': contacts})

@login_required(login_url='login')
def create_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            return redirect('gerer_contact')
    else:
        form = ContactForm()
    return render(request, 'create_contact.html', {'form': form})

@login_required(login_url='login')
def update_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('gerer_contact')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'update_contact.html', {'form': form})

@login_required(login_url='login')
def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk, owner=request.user)
    if request.method == 'POST':
        contact.delete()
        return redirect('gerer_contact')
    return render(request, 'delete_contact.html', {'contact': contact})


