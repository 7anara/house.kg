from django.contrib import admin
from .models import UserProfile, Country, Region, City, District, Property, PropertyImages, Review
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin


class RegionInline(admin.TabularInline, TranslationInlineModelAdmin):
    model = Region
    extra = 1


@admin.register(Country)
class CountryAdmin(TranslationAdmin):
    inlines = [RegionInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class DistrictInline(admin.TabularInline, TranslationInlineModelAdmin):
    model = District
    extra = 1

@admin.register(City)
class CityAdmin(TranslationAdmin):
    inlines = [DistrictInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class PropertyImageInline(admin.TabularInline):
    model = PropertyImages
    extra = 1


@admin.register(Property)
class PropertyAdmin(TranslationAdmin):
    inlines = [PropertyImageInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(UserProfile),
admin.site.register(Review),