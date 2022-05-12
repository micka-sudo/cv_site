from django.shortcuts import render
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail


# def contact_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             email_subject = f'New contact {form.cleaned_data["email"]}: {form.cleaned_data["subject"]}'
#             email_message = form.cleaned_data['message']
#             send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAIL)
#             return render(request, 'contact/success.html')
#     form = ContactForm()
#     context = {'form': form}
#     return render(request, 'contact/contact.html', context)
def contact_view(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            prenom = form.cleaned_data['prenom']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            titre = f'blog | {nom} {prenom} - {email}'
            send_mail(titre, message, 'mickael.gerard.site@gmail.com', ['mickael.gerard.site@gmail.com'])
        return HttpResponseRedirect(reverse('remerciements'))
    return render(request, 'contact/contact.html', {"form": form})