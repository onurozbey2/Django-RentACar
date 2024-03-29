"""RentACar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from home import views

urlpatterns = [
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('cars/', include('cars.urls')),
    path('user/', include('user.urls')),
    path('admin/', admin.site.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

    path('hakkimizda/', views.hakkimizda, name='hakkimizda'),
    path('referanslarimiz/', views.referanslarimiz, name='referanslarimiz'),
    path('iletisim/', views.iletisim, name='iletisim'),
    path('uye_kayit/', views.uye_kayit, name='uye_kayit'),
    path('uye_giris/', views.uye_giris, name='uye_giris'),
    path('logout/', views.logout_view, name='logout_view'),
    path('araclar/', views.araclar, name='araclar'),
    path('arac_detaylar/<int:id>/<slug:slug>/',
         views.arac_detaylar, name='arac_detaylar'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
