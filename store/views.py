from rest_framework import viewsets, generics, status
from .models import  UserProfile, Country, Region, City, District, Property, PropertyImages, Review
from .serializers import (UserProfileSerializer, CountryListSerializer,
                          CountryDetailSerializer, RegionListSerializer, RegionDetailSerializer,
                          CityListSerializer, CityDetailSerializer,
                          DistrictListSerializer, DistrictDetailSerializer,
                          PropertyListSerializer, PropertyDetailSerializer,
                          PropertyImageSerializer, ReviewSerializer,
                          UserRegisterSerializer, LoginSerializer)


from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError

class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({"detail": "Неверные учетные данные"}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            if not refresh_token:
                return Response({'detail': 'Refresh токен не предоставлен.'}, status=status.HTTP_400_BAD_REQUEST)
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'detail': 'Вы успешно вышли.'}, status=status.HTTP_200_OK)
        except TokenError as e:
            return Response({'detail': 'Недействительный токен.'}, status=status.HTTP_400_BAD_REQUEST)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)

class CountryListAPIView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryListSerializer

class CountryDetailAPIView(generics.RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryDetailSerializer

class RegionListAPIView(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionListSerializer

class RegionDetailAPIView(generics.RetrieveAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionDetailSerializer

class CityListAPIView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CityListSerializer

class CityDetailAPIView(generics.RetrieveAPIView):
    queryset = City.objects.all()
    serializer_class = CityDetailSerializer

class DistrictListAPIView(generics.ListAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictListSerializer

class DistrictDetailAPIView(generics.RetrieveAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictDetailSerializer


class PropertyListAPIView(generics.ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertyListSerializer

class PropertyDetailAPIView(generics.RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertyDetailSerializer

class PropertyImageViewSet(viewsets.ModelViewSet):
    queryset = PropertyImages.objects.all()
    serializer_class = PropertyImageSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer