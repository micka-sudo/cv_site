from django.shortcuts import render
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            email_subject = f'New contact {form.cleaned_data["Email"]}: {form.cleaned_data["Sujet"]}'
            email_message = form.cleaned_data['Message']
            send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAIL)
            return render(request, 'contact/succes.html')
    form = ContactForm()
    return render(request, 'contact/contact.html', context={'form': form})
# def contact_view(request):
#     form = ContactForm()
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             nom = form.cleaned_data['nom']
#             prenom = form.cleaned_data['prenom']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']
#             titre = f'blog | {nom} {prenom} - {email}'
#             send_mail(titre, message, 'mickael.gerard.site@gmail.com', ['mickael.gerard.site@gmail.com'])
#         return HttpResponseRedirect(reverse('remerciements'))
#     return render(request, 'contact/contact.html', {"form": form})
#
#
# def remerciements_view(request):
#     return render(request, 'contact/succes.html')
