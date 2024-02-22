from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    category_name = models.CharField(max_length = 100)
    category_id = models.PositiveIntegerField()
    
    def __str__(self):
        return self.category_name

class Product(models.Model):
    category_name = models.ForeignKey(ProductCategory, related_name = 'pros', on_delete = models.CASCADE)
    product_id = models.PositiveIntegerField(unique = True)
    product_name = models.CharField(max_length = 100)
    cost = models.DecimalField(max_digits = 6, decimal_places = 2)
    date = models.DateField(auto_now = True)   
    
    def __str__(self):
        return self.product_name