from django.db import models


class Cars(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    keywords = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    model_year = models.CharField(max_length=200)
    engine_capacity = models.CharField(max_length=200)
    gear = models.CharField(max_length=200)
    fuel = models.CharField(max_length=200)
    body_type = models.CharField(max_length=200)
    image = models.ImageField(blank=True, upload_to='images/')
    slug = models.SlugField()
    status = models.CharField(max_length=20, choices=STATUS)
    create_at = models.DateTimeField('date published')
    update_at = models.DateTimeField('date published')

    def __str__(self):
        return self.brand
