from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Category(MPTTModel):
    name = models.CharField(max_length=250)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children')
    published = models.BooleanField(default=True)
    
    class MPTTMeta:
        order_by_insertion = ['name']
        
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ['parent__name']
        verbose_name="Category"
        verbose_name_plural="Categories"
        
    
