from django.http import HttpResponseRedirect, HttpResponse
from cars.models import CommentForm, Comment, Reservation, ReservationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    return HttpResponse("You're at the CARS index.")


@login_required(login_url='/login')   # login kontrol
def addcomment(request, id):
    url = request.META.get('HTTP_REFERER')  # get last url
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            current_user = request.user

            data = Comment()
            data.user_id = current_user.id
            data.car_id = id
            data.name = form.cleaned_data['name']
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(
                request, "Yorumunuz gönderilmiştir. Teşekkür ederiz.")
            return HttpResponseRedirect(url)
    messages.error(
        request, "Yorumunuz kaydedilmedi. Lütfen kontrol edin.")
    return HttpResponseRedirect(url)


@login_required(login_url='/login')   # login kontrol
def addreservation(request, id):
    url = request.META.get('HTTP_REFERER')  # get last url
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            current_user = request.user

            data = Reservation()
            data.user_id = current_user.id
            data.car_id = id
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.phone = form.cleaned_data['phone']
            data.address = form.cleaned_data['address']
            data.checkin = form.cleaned_data['checkin']
            data.checkout = form.cleaned_data['checkout']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(
                request, "Rezervasyon işlemi tamamlanmıştır. Teşekkür ederiz.")
            return HttpResponseRedirect(url)
    messages.warning(
        request, "Rezervasyon kaydedilmedi. Lütfen kontrol edin.")
    return HttpResponseRedirect(url)
