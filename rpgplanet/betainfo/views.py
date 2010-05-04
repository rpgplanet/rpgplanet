# -*- coding: utf-8 -*-
from django.views.generic.simple import direct_to_template

from django.forms import Form, EmailField, ValidationError

from betainfo.models import BetaCandidate

class EmailForm(Form):
    email = EmailField()

    def clean_email(self):
        data = self.cleaned_data['email']
        if BetaCandidate.objects.filter(email=data).count() > 0:
            raise ValidationError(u"Tento e-mail je již registrován. Díky za přízeň!")
        return data

def registration(request):
    message = ''
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            BetaCandidate.objects.create(
                email=form.cleaned_data['email']
            )
            message = u"E-mail zaznamenán, díky za přízeň! Rádi se ozveme."
    else:
        form = EmailForm()

    return direct_to_template(request, 'betainfo/registration.html', {
        'form' : form,
        'message' : message
    })

