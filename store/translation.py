from .models import Country, Region,City, District, Property
from modeltranslation.translator import TranslationOptions,register

@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('country_name',)


@register(Region)
class RegionTranslationOptions(TranslationOptions):
    fields = ('region_name', )



@register(City)
class CityTranslationOptions(TranslationOptions):
    fields = ('city_name', )


@register(District)
class DistrictTranslationOptions(TranslationOptions):
    fields = ('district_name', )


@register(Property)
class PropertyTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'address', 'condition')