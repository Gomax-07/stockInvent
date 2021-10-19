from django.db import models 
from django.utils import timezone
# from django.contrib.auth.models import User
# from users.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse


class Supplier(models.Model):
    id = models.IntegerField(primary_key=True)
    # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=120, unique=True)
    address = models.CharField(max_length=220)
    created_date = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=250,null=False, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug
        }
        return reverse('supplier_detail', kwargs=kwargs)
    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value,)
        super().save(*args, **kwargs)


class Buyer(models.Model):
    id = models.IntegerField(primary_key=True)
    # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=120, unique=True)
    address = models.CharField(max_length=220)
    created_date = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=250,null=False, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug
        }
        return reverse('buyer_detail', kwargs=kwargs)
    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value,)
        super().save(*args, **kwargs)


class Season(models.Model):
    name = models.CharField(max_length=120, unique=True)
    description = models.CharField(max_length=220)
    created_date = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=250,null=False, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug
        }
        return reverse('season_detail', kwargs=kwargs)
    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value,)
        super().save(*args, **kwargs)


class Drop(models.Model):
    name = models.CharField(max_length=120, unique=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
        


class Product(models.Model):
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=250,null=False, unique=True) 
    sortno = models.PositiveIntegerField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug
        }
        return reverse('product_detail', kwargs=kwargs)
    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value,)
        super().save(*args, **kwargs)


class Order(models.Model):
    STATUS_CHOICE = (
        ('pending', 'Pending'),
        ('decline', 'Decline'),
        ('approved', 'Approved'),
        ('processing', 'Processing'),
        ('complete', 'Complete'),
        ('bulk', 'Bulk'),
    )
    supplier = models.CharField(max_length=50)
    product = models.CharField(max_length=50)
    design = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    buyer = models.CharField(max_length=50)
    season =models.CharField(max_length=50)
    drop =models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)
    created_date = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=250,null=False, unique=True)

    def __str__(self):
        return self.product.name

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug
        }
        return reverse('order_detail', kwargs=kwargs)
    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value,)
        super().save(*args, **kwargs)


class Delivery(models.Model):
    id = models.IntegerField(primary_key=True)
    order =models.CharField(max_length=50)
    courier_name = models.CharField(max_length=120)
    created_date = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=250,null=False, unique=True)

    def __str__(self):
        return self.courier_name

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug
        }
        return reverse('delivery_detail', kwargs=kwargs)
    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value,)
        
        super().save(*args, **kwargs)

