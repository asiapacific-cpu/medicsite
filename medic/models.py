from django.db import models
from django.urls import reverse
from django.utils.text import slugify
import ast

class ListField(models.TextField):
    description = "Stores a python list"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        if isinstance(value, str):
            return value.split('-')

    def to_python(self, value):
        if not value:
            value = []
        if isinstance(value, list):
            return value
        if isinstance(value, str):
            return ast.literal_eval(value)

    def get_prep_value(self, value):
        if value is None:
            return value
        if value is not None and isinstance(value, str):
            return value
        if isinstance(value, list):
            return '-'.join(value)

    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return self.get_prep_value(value)


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    description = ListField()

    active = models.BooleanField(default=True)
    categories = models.ManyToManyField('Category', blank=True)
    product_categories = models.ManyToManyField('ProductCategory', blank=True)
    product_default = models.ForeignKey('ProductCategory', related_name='default_productcategory', null=True, blank=True,
                                on_delete=models.CASCADE)
    default = models.ForeignKey('Category', related_name='default_category', null=True, blank=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def get_image_url(self):
        img = self.itemimage_set.first()
        if img:
            return img.image.url
        return img



def image_upload_to(instance, filename):
    title = instance.item.title
    slug = slugify(title)
    basename, file_extension = filename.split(".")
    new_filename = "%s-%s.%s" % (basename, instance.id, file_extension)
    return "static/img/%s/%s" % (slug, new_filename)


class ItemImage(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload_to)



class Category(models.Model):
    title = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(unique=True)
    categoryimage = models.ImageField(upload_to='category_images')
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("products_detail", kwargs={"slug": self.slug})


class ProductCategory(models.Model):
    title = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(unique=True)
    categoryimage = models.ImageField(upload_to='category_images')
    categories = models.ManyToManyField('Category', blank=True)
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("item_detail", kwargs={"slug": self.slug})
