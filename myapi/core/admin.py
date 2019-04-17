from django.contrib import admin

from core.models import Category, Ad



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'tell', 'category', 'owner', 'created')
    list_filter = ('category', 'created')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Ad, AdAdmin)