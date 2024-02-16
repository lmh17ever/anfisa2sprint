from django.contrib import admin

# Register your models here.
from .models import Category, Topping, IceCream


class IceCreamAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper',
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category',
    )
    search_fields = ('title', )
    list_filter = ('category', )
    list_display_links = ('title', )
    filter_horizontal = ('toppings', )


class IceCreamInLine(admin.TabularInline):
    model = IceCream
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        IceCreamInLine,
    )
    list_display = (
        'title',
    )


admin.site.register(Topping)
admin.site.register(IceCream, IceCreamAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.empty_value_display = 'Не задано'
