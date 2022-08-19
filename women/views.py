from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives

from .forms import ContactForm

from .models import *



def index(request):
    return render(request, 'women/index.html')
    
def about(request):
    return render(request, 'women/about.html')
    
def fotogalerie(request):
    return render(request, 'women/fotogalerie.html')

def cenik(request):
    return render(request, 'women/cenik.html')

def kontact(request):
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_message(form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['message'])
            context = {'success': 1}
    else:
        form = ContactForm()
    context['form'] = form
    return render(request, 'women/kontact.html',context=context)


def send_message(name, email, message):
    text = get_template('women/message.html')
    html = get_template('women/message.html')
    context = {'name': name, 'email': email, 'message': message}
    subject = 'Сообщение от пользователя'
    from_email = 'from@example.com'
    text_content = text.render(context)
    html_content = html.render(context)

    msg = EmailMultiAlternatives(subject, text_content, from_email, ['vladik.miduan@gmail.com'])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()