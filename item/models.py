from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Category(models.Model):
    """
    Model for Category
    """
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('name', )
    
    def __str__(self):
        return self.name
        

class Item(models.Model):
    """
    Model for Item
    """
    name = models.CharField(max_length=75)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(null=False, decimal_places=2, validators=[MinValueValidator(0.01)], max_digits=10)
    is_sold = models.BooleanField(default=False)
    image = models.ImageField(upload_to='item_images', blank= True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
    
    def __str__(self):
        return self.name
    