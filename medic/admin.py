from django.contrib import admin
from .models import Item, ItemImage, Category, ProductCategory
# Register your models here.

class ItemImageInline(admin.TabularInline):
    model = ItemImage
    extra = 0
    max_num = 5


class ItemAdmin(admin.ModelAdmin):
    inlines = [
        ItemImageInline,
    ]
    class Meta:
        model = Item


admin.site.register(Item, ItemAdmin)


class ItemImageAdmin(admin.ModelAdmin):
    list_display = ["item", "image"]

    class meta:
        model = ItemImage

admin.site.register(ItemImage,ItemImageAdmin)




class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}
    class Meta:
        model = Category
admin.site.register(Category,CategoryAdmin)



class ProductCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}
    class Meta:
        model = ProductCategory
admin.site.register(ProductCategory,ProductCategoryAdmin)