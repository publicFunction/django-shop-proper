from django.db import models

from categories.models import Category

class Product(models.Model):
    category = models.ForeignKey(Category)
    #gallery = models.ForeignKey()
    #feature_image = models.ImageField(upload_to='uploads/products/feature_images/')
    name = models.CharField(max_length=350)
    price = models.FloatField()
    
    def __unicode__(self):
        return self.name
    
    def with_category(self):
        return "%s in %s" % (self.name, self.category) 
    
    class Meta:
        verbose_name="Product"
        verbose_name_plural="Products"
    
class ProductVariationType(models.Model):
    product = models.ForeignKey('Product')
    type = models.CharField(max_length=350)
    
    def __unicode__(self):
        return "%s for %s" % (self.type, self.product)
    
    class Meta:
        verbose_name="Product Variation"
        verbose_name_plural="Product Variations"
    
class ProductVariationOption(models.Model):
    variation = models.ForeignKey('ProductVariationType')
    option = models.CharField(max_length=350)
    
    def __unicode__(self):
        return "%s in %s" % (self.option, self.variation)
    
    class Meta:
        verbose_name="Product Variation Option"
        verbose_name_plural="Product Variations Options"
