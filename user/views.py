from django.shortcuts import render
from home.models import Setting, UserProfile
# Create your views here.


def index(request):
    setting = Setting.objects.get(pk=1)
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {'setting': setting,
               'profile': profile}
    return render(request, 'uye_profil.html', context)
