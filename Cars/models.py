from django.db import models
from django.utils.safestring import mark_safe
from django.db.models import TextField
from ckeditor_uploader.fields import RichTextUploadingField


class Cars(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    marka = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    keywords = models.CharField(max_length=200)
    fiyat = models.CharField(max_length=200)
    model_yılı = models.CharField(max_length=200)
    motor_hacmi = models.CharField(max_length=200)
    vites = models.CharField(max_length=200)
    yakıt = models.CharField(max_length=200)
    kasa_tipi = models.CharField(max_length=200)
    resim = models.ImageField(blank=True, upload_to='images/')
    detay = RichTextUploadingField(blank=True)
    durum = models.CharField(max_length=20, choices=STATUS)
    ilan_tarihi = models.DateTimeField('date published')

    def __str__(self):
        return self.marka

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.resim.url))
    image_tag.short_description = 'Resim'


class Images(models.Model):
    cars = models.ForeignKey(Cars, on_delete=models.CASCADE)
    title = models.CharField(blank=True, max_length=50)
    resim = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.resim.url))
    image_tag.short_description = 'Resim'
