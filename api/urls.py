from django.urls import path

from api import views

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router=DefaultRouter()

urlpatterns=[
    path('register/',views.SignUpView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]+router.urls