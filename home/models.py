from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Setting(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    company = models.CharField(max_length=50)
    address = models.CharField(blank=True, max_length=200)
    phone = models.CharField(blank=True, max_length=20)
    email = models.CharField(blank=True, max_length=30)
    smptserver = models.CharField(blank=True, max_length=20)
    smptemail = models.CharField(blank=True, max_length=20)
    smptpassword = models.CharField(blank=True, max_length=20)
    smtpport = models.CharField(blank=True, max_length=5)
    icon = models.ImageField(blank=True, upload_to='images/')
    facebook = models.CharField(blank=True, max_length=100)
    instagram = models.CharField(blank=True, max_length=100)
    twitter = models.CharField(blank=True, max_length=100)
    aboutus = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    references = RichTextUploadingField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
