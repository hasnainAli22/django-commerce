from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = 'categories'
    
    
    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    brand = models.CharField(max_length=250, default='un-branded')
    price = models.DecimalField(max_digits=10,decimal_places=2)
    slug = models.SlugField(max_length=250)
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'products'
    
    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self):
        return reverse('store:product_detail', kwargs={'product_slug': self.slug})
    
    
