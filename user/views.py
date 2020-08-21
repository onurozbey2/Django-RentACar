from django.shortcuts import render
from home.models import Setting, UserProfile
from cars.models import Reservation, Comment
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    setting = Setting.objects.get(pk=1)
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {'setting': setting,
               'profile': profile}
    return render(request, 'uye_profil.html', context)


@login_required(login_url='/login')
def rezervasyonlar(request):
    setting = Setting.objects.get(pk=1)
    current_user = request.user
    reservations = Reservation.objects.filter(user_id=current_user.id)
    context = {'setting': setting,
               'reservations': reservations}
    return render(request, 'rezervasyonlar.html', context)


@login_required(login_url='/login')
def yorumlar(request):
    setting = Setting.objects.get(pk=1)
    current_user = request.user
    comments = Comment.objects.filter(user_id=current_user.id)
    context = {'setting': setting,
               'comments': comments}
    return render(request, 'yorumlar.html', context)
