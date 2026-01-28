from rest_framework import serializers
from .models import UserProfile, Country, Region, City, District, Property, PropertyImages, Review



from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name', 'phone_number', )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user




class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']



class CityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['city_name', 'city_image',]


class DistrictListSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['district_name', ]


class DistrictDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['id', 'district_name',  ]


class CityDetailSerializer(serializers.ModelSerializer):
    districts = DistrictListSerializer(many=True, read_only=True)

    class Meta:
        model = City
        fields = ['id', 'city_name', 'city_image', 'districts']


class RegionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['region_name', ]


class RegionDetailSerializer(serializers.ModelSerializer):
    cities = CityListSerializer(many=True, read_only=True)
    class Meta:
        model = Region
        fields = ['id', 'region_name', 'cities']


class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name', ]

class CountryDetailSerializer(serializers.ModelSerializer):
    regions = RegionListSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ['id', 'country_name', 'regions']


class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImages
        fields = ['property_image']


class ReviewSerializer(serializers.ModelSerializer):
    author = UserProfileSimpleSerializer(read_only=True)
    seller = UserProfileSimpleSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'author', 'seller', 'rating', 'comment']

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'


class PropertyListSerializer(serializers.ModelSerializer):
    images = PropertyImageSerializer(many=True, read_only=True)
    city = CityListSerializer(read_only=True)

    class Meta:
        model = Property
        fields = [
           'title', 'city',
            'area', 'price', 'images',
        ]


class PropertyDetailSerializer(serializers.ModelSerializer):
    seller = UserProfileSerializer(read_only=True)
    images = PropertyImageSerializer(many=True, read_only=True)
    city = CityListSerializer(read_only=True)
    region = RegionListSerializer(read_only=True)
    district = DistrictListSerializer(read_only=True)
    reviews = ReviewSerializer(source='seller.reviews_received', many=True, read_only=True)

    class Meta:
        model = Property
        fields = [
            'id', 'title', 'description', 'property_type', 'region', 'city', 'district',
            'address', 'area', 'price', 'rooms', 'floor', 'total_floors', 'condition',
            'documents', 'seller', 'images', 'reviews'
        ]



