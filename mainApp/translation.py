from .models import Product
from modeltranslation.translator import TranslationOptions, register

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description')