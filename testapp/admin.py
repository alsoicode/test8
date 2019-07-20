from .models import Test, SortTest
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from adminsortable.admin import SortableAdmin


@admin.register(Test)
class TestAdmin(TranslationAdmin):
    pass


@admin.register(SortTest)
class SortTestAdmin(SortableAdmin, TranslationAdmin):
    pass
