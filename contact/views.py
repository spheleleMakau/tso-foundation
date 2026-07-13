from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()

        if name and email and subject and message:
            send_mail(
                f'TSO Foundation contact: {subject}',
                f'Name: {name}\nEmail: {email}\nPhone: {phone}\n\n{message}',
                email,
                ['hello@tsocentre.org'],
                fail_silently=True,
            )
            messages.success(request, 'Thank you for your message. We will get back to you soon.')
            return HttpResponseRedirect(reverse('contact:thanks'))

        messages.error(request, 'Please complete all required fields before submitting.')

    return render(request, 'contact/contact.html')


def thanks(request):
    return render(request, 'contact/thanks.html')
