from django.contrib import admin
from django.contrib.admin.filters import SimpleListFilter
from django.utils.translation import ugettext_lazy as _

from categories.models import Category

class ByParentFilter(SimpleListFilter):
    title = _('Parents')
    parameter_name = "parent"
    
    def lookups(self, request, model_admin):
        qs = model_admin.queryset(request)
        if qs.filter(parent__isnull=True).exists():
            yield ('show_parent_only', _('List Parent Categories Only'))
    
    def queryset(self, request, queryset):
        if self.value() == 'show_parent_only':
            return queryset.filter(parent__isnull=True)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent',)
    list_filter = (ByParentFilter,)

admin.site.register(Category, CategoryAdmin)