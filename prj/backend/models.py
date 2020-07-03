from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=40, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'



class Subcategory(models.Model):
    name = models.CharField(max_length=40, default='')
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )

    def __str__(self):
        return '{}({})'.format(self.name, self.category)

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

class Enterprises(models.Model):
    name = models.CharField(max_length=250, default='')
    content = models.TextField(default='')
    image = models.ImageField(upload_to='images')
    city = models.CharField(max_length=30, default='')
    address = models.CharField(max_length=250, default='')
    phone = models.CharField(max_length=20, default='')
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )
    subcategory = models.ForeignKey(
        Subcategory, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )

    def __str__(self):
        return '{}({})'.format(self.name, self.subcategory)

    class Meta:
        verbose_name = 'Предприятие'
        verbose_name_plural = 'Предприятия'


