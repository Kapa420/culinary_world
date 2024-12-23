from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image
from io import BytesIO

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
    
    def save(self, *args, **kwargs):
        if self.image:
            image = Image.open(self.image)


            if image.format != 'WEBP':
                image = image.resize((800,600))
                new_filename = f"{self.name}_{self.category.name}.webp"

                output = BytesIO()
                image.save(output, format='WEBP', quality=90)
                output.seek(0)

                self.image = InMemoryUploadedFile(
                    output,
                    'ImageField',
                    new_filename,
                    'image/webp',
                    output.getbuffer().nbytes,
                    None,
                    'utf-8'
                )

        super(Item, self).save(*args, **kwargs)
    