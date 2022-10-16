from django.db import models
from django.urls import reverse
import uuid
from datetime import date
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(null=True, blank=True)


class Category(models.Model):
    name = models.CharField('Category name', max_length=200, help_text='Enter category')

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField('Manufacturer name', max_length=200)
    country_origin = models.CharField('Manufacturer country of origin', max_length=200)
    description = models.CharField('Manufacturer description', max_length=500)

    def get_absolute_url(self):
        return reverse('manufacturer', args=[str(self.id)])

    def __str__(self):
        return f'{self.name} ({self.country_origin})'


class Tool(models.Model):
    title = models.CharField('Title', max_length=200)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.SET_NULL, null=True, related_name='tools')
    date_production = models.DateField('Production date', null=True, blank=True)
    category = models.ManyToManyField('Category', help_text='Choose category')
    ean_code = models.CharField('EAN', max_length=13, help_text='13 symbols')
    image = models.ImageField('Image', upload_to='images', null=True, blank=True)

    def get_absolute_url(self):
       return reverse('tool-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.title} ({self.manufacturer.name}, {self.manufacturer.country_origin}, {self.ean_code}, {self.date_production})'

    def display_category(self):
        return ', '.join(category.name for category in self.category.all()[:3])

    display_category.short_description = 'Category'


class ToolCopy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for tool copy')
    tool = models.ForeignKey('Tool', on_delete=models.CASCADE, null=True)
    due_back = models.DateField('Due back', null=True, blank=True)

    LOAN_STATUS = (

        ('a', 'Available'),
        ('b', 'Borrowed'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='a', help_text='Status')
    price = models.FloatField()
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
       return f'{self.tool.title}, {self.price} eur, {self.status}, ({self.tool.manufacturer.name}, {self.tool.manufacturer.country_origin}, {self.tool.ean_code})'

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    def get_absolute_url(self):
        return reverse('tool-detail', args=[str(self.id)])
