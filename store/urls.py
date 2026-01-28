from .views import (UserProfileViewSet, CountryListAPIView, CountryDetailAPIView,
                    RegionListAPIView, RegionDetailAPIView, CityListAPIView, CityDetailAPIView,
                    DistrictListAPIView, DistrictDetailAPIView,
                    RegisterView, LoginView, LogoutView,PropertyListAPIView,
                    PropertyDetailAPIView, PropertyImageViewSet, ReviewViewSet, )
from rest_framework import routers
from django.urls import path, include


router = routers.SimpleRouter()
router.register(r'user', UserProfileViewSet, basename='user')
router.register(r'propertyImage', PropertyImageViewSet, basename='image')
router.register(r'review', ReviewViewSet, basename='review')


urlpatterns = [
    path('', include(router.urls)),

    path('register', RegisterView.as_view(), name='registrations'),
    path('login', LoginView.as_view(), name = 'login'),
    path('logout', LogoutView.as_view(), name = 'logout'),


    path('country/', CountryListAPIView.as_view()),
    path('country/<int:pk>/', CountryDetailAPIView.as_view()),
    path('region/', RegionListAPIView.as_view()),
    path('region/<int:pk>/', RegionDetailAPIView.as_view()),
    path('city/', CityListAPIView.as_view()),
    path('city/<int:pk>/', CityDetailAPIView.as_view()),
    path('district/', DistrictListAPIView.as_view()),
    path('district/<int:pk>/', DistrictDetailAPIView.as_view()),
    path('property/', PropertyListAPIView.as_view()),
    path('property/<int:pk>/', PropertyDetailAPIView.as_view()),
]

