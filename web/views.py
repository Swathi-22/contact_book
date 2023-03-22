from django.shortcuts import render, redirect
from .models import Contact



def contact_list(request):
    contacts = Contact.objects.all()
    context =  {'contacts': contacts}
    return render(request, 'contact_list.html',context)


def contact_detail(request, pk):
    contact = Contact.objects.get(pk=pk)
    context = {'contact': contact}
    return render(request, 'contact_detail.html',context )


def contact_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        if Contact.objects.filter(phone_number=phone_number).exists():
            error_message = f"{phone_number} already exists in your contacts."
            context = {'error_message': error_message}
            return render(request, 'contact_form.html',context)
        else:
            new_contact = Contact(name=name, phone_number=phone_number)
            new_contact.save()
            return redirect('web:contact_list')
    return render(request, 'contact_form.html')


def contact_update(request, pk):
    contact = Contact.objects.get(pk=pk)
    if request.method == 'POST':
        contact.name = request.POST['name']
        contact.phone_number = request.POST['phone_number']
        contact.save()
        return redirect('web:contact_list')
    context = {'contact': contact}
    return render(request, 'contact_form.html',context)


def contact_delete(request, pk):
    contact = Contact.objects.get(pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('web:contact_list')
    context = {'contact': contact}
    return render(request,'contact_confirm_delete.html',context)


def handler404(request, exception):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)