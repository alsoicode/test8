from modeltranslation.translator import register, TranslationOptions
from .models import Test, SortTest


@register(Test)
class TestTranslationOptions(TranslationOptions):
    fields = ('test',)


@register(SortTest)
class SortTestTranslationOptions(TranslationOptions):
    pass
