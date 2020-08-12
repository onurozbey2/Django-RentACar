# from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from home.models import Setting, ContactForm, ContactMessageForm
from django.http import HttpResponseRedirect

from cars.models import Cars


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Cars.objects.all()[:5]
    context = {'setting': setting,
               'page': 'home',
               'sliderdata': sliderdata}
    return render(request, 'index.html', context)


def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'hakkimizda'}
    return render(request, 'hakkimizda.html', context)


def referanslarimiz(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'referanslarimiz'}
    return render(request, 'referanslarimiz.html', context)


def iletisim(request):
    if request.method == 'POST':  # check post
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessageForm()  # create relation with model
            data.name = form.cleaned_data['name']  # get form input data
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()  # save data to table
            messages.success(
                request, "Mesajınız başarı ile gönderildi. Teşekkür ederiz.")
            return HttpResponseRedirect('/iletisim')

    setting = Setting.objects.get(pk=1)
    form = ContactForm()
    context = {'setting': setting, 'page': 'iletisim'}
    return render(request, 'iletisim.html', context)
