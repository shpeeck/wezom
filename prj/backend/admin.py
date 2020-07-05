from django.contrib import admin
from backend.models import Category, Subcategory, Enterprises, StaticPage

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)

class SubcategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Subcategory, SubcategoryAdmin)

class EnterprisesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Enterprises, EnterprisesAdmin)

class StaticPageAdmin(admin.ModelAdmin):
    pass

admin.site.register(StaticPage, StaticPageAdmin)