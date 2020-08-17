from django.db import models
from django.forms import ModelForm
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
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
    slug = models.SlugField(blank=True, max_length=200)
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


class Comment(models.Model):
    STATUS = (
        ('New', 'Yeni'),
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    car = models.ForeignKey(Cars, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    subject = models.CharField(blank=True, max_length=30)
    comment = models.TextField(max_length=500)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'comment']
