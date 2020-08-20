from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

from home.forms import SignUpForm
from home.models import Setting, ContactForm, ContactMessageForm
from cars.models import Cars, Images, Comment


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Cars.objects.all()[:5]
    homelastrentals = Cars.objects.all().order_by('?')[:6]
    context = {'setting': setting,
               'page': 'home',
               'sliderdata': sliderdata,
               'homelastrentals': homelastrentals}
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


def araclar(request):
    setting = Setting.objects.get(pk=1)
    cars = Cars.objects.all()
    context = {'setting': setting, 'cars': cars}
    return render(request, 'araclar.html', context)


def arac_detaylar(request, id, slug):
    setting = Setting.objects.get(pk=1)
    cardetail = Cars.objects.get(pk=id)
    images = Images.objects.get(cars_id=id)
    comments = Comment.objects.filter(car_id=id, status='True')
    context = {'setting': setting, 'cardetail': cardetail,
               'images': images, 'comments': comments}
    return render(request, 'arac_detaylar.html', context)


def uye_kayit(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/')
    setting = Setting.objects.get(pk=1)
    form = SignUpForm()
    context = {'setting': setting, 'page': 'uye_giris', 'form': form}
    return render(request, 'uye_kayit.html', context)


def uye_giris(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect('/')
        else:
            # Return an 'invalid login' error message.
            messages.warning(
                request, "Giriş hatası! Bilgilerinizi kontrol edin!")
            return HttpResponseRedirect('/uye_giris')

    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'uye_giris'}
    return render(request, 'uye_giris.html', context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')   # Redirect to a success page.
