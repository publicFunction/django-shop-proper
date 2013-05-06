from django.contrib import admin
#from django.contrib.admin.filters import SimpleListFilter
#from django.utils.translation import ugettext_lazy as _

from products.models import Product, ProductVariationType, ProductVariationOption

'''class ByParentFilter(SimpleListFilter):
    title = _('Parents')
    parameter_name = "parent"
    
    def lookups(self, request, model_admin):
        qs = model_admin.queryset(request)
        if qs.filter(parent__isnull=True).exists():
            yield ('show_parent_only', _('List Parent Categories Only'))
        if qs.filter(parent__isnull=False).exists():
            yield ('children', _('List Child Categories Only'))
    
    def queryset(self, request, queryset):
        if self.value() == 'show_parent_only':
            return queryset.filter(parent__isnull=True)
        if self.value() == 'children':
            return queryset.filter(parent__isnull=False)
'''

class ProductVariationTypeInline(admin.TabularInline):
    model = ProductVariationType

class ProductVariationOptionInline(admin.TabularInline):
    model = ProductVariationOption

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductVariationTypeInline,]
    list_display = ('name', 'category',)
    list_filter = ('category',)

class ProductVariationTypeAdmin(admin.ModelAdmin):
    inlines = [ProductVariationOptionInline,]
    list_display = ('type', 'product',)
    list_filter = ('type',)


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductVariationType, ProductVariationTypeAdmin)
