from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=250)
    parent = models.ForeignKey('self', blank=True, null=True)
    published = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ['parent__name']
        verbose_name="Category"
        verbose_name_plural="Categories"
