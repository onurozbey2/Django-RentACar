from django.db import models


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
    durum = models.CharField(max_length=20, choices=STATUS)
    ilan_tarihi = models.DateTimeField('date published')
    # update_at = models.DateTimeField('date published')

    def __str__(self):
        return self.marka


class Images(models.Model):
    cars = models.ForeignKey(Cars, on_delete=models.CASCADE)
    title = models.CharField(blank=True, max_length=50)
    resim = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title
